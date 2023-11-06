import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.feature_extraction import DictVectorizer

import xgboost as xgb
from sklearn.metrics import roc_curve, auc, roc_auc_score
import pickle

# parameters
eta = 0.1
max_depth = 10
min_child_weight = 1
num_boost_round = 150


n_splits = 5
output_file = f'model_xgb.bin'
train_data = "./data/adult.data"
test_data = "./data/adult.test"

columns=('age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income')

categorical = ['workclass', 'education', 'marital_status', 'occupation',
       'relationship', 'race', 'sex', 'native_country']
numerical = ['age', 'capital_gain', 'capital_loss','hours_per_week']


def read_prepare_data(filename: str, is_test_data: bool = False):
    if is_test_data:
        df = pd.read_csv(filename, names = columns, skiprows=1)
    else:
        df = pd.read_csv(filename, names = columns)

    df.columns = df.columns.str.lower().str.replace('-', '_')
    categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)
    for col in categorical_columns:
        df[col] = df[col].str.lower().str.strip().str.replace('-', '_')

    df = df.replace('?', np.nan)
    df = df.dropna()

    if is_test_data:
        df['income>50k'] = (df['income'] == '>50k.').astype(int)
    else:
        df['income>50k'] = (df['income'] == '>50k').astype(int)

    return df


df_full_train = read_prepare_data(train_data)
df_test = read_prepare_data(test_data, is_test_data=True)

# training
def train(df_train, y_train):
    dicts = df_train[categorical + numerical].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=dv.feature_names_)

    xgb_params = {
        'eta': eta,
        'max_depth': max_depth,
        'min_child_weight': min_child_weight,

        'objective': 'binary:logistic',
        'eval_metric': 'auc',
        'nthread': 8,

        'seed': 1,
        'verbosity': 1,
    }

    model = xgb.train(xgb_params, dtrain, 
                    num_boost_round = num_boost_round)

    return dv, model

# prediction
def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')

    X=dv.transform(dicts)
    dval = xgb.DMatrix(X, feature_names=dv.feature_names_)
    
    y_pred = model.predict(dval)
    return y_pred


# validation
Kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)

scores = []
fold = 0
for train_idx, test_idx in Kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[test_idx]

    y_train = df_train['income>50k'].values
    y_val = df_val['income>50k'].values

    dv, model = train(df_train, y_train)
    y_pred = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)

    print(f'auc on fold {fold} is {auc}')
    fold = fold + 1

print('validation results:')   
print('%.3f +- %.3f' % (np.mean(scores), np.std(scores)))


print('training the final model...')
dv, model = train(df_full_train, df_full_train['income>50k'].values)
y_pred = predict(df_test, dv, model)

y_test = df_test['income>50k'].values
auc = roc_auc_score(y_test, y_pred)
print(f'auc={auc}')


# Save the model
with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')
