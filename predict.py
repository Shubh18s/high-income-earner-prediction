import pickle
from flask import Flask
from flask import request
from flask import jsonify
import xgboost as xgb

input_file = 'model_xgb.bin'

with open(input_file, 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

app = Flask('high income prediction')

@app.route('/predict', methods=['POST'])
def predict():
  person = request.get_json()
  high_income = generate_prediction(person)

  result = {
    'high_income' : bool(high_income)
  }
  return jsonify(result)

def generate_prediction(person):
  X = dv.transform([person])
  dtest = xgb.DMatrix(X, feature_names=dv.feature_names_)
  
  y_pred = model.predict(dtest)

  return (y_pred)

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=9696)