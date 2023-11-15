# High income earner prediction
The project predicts high income (>$50k/yr.) earners from 1994 census data.

## Task
Based on the attributes of an individual such as age, education,
marital-status, occupation, race etc. we try to predict whether they earn over $50k/year. The `fnwgt` feature represents the weight for a particular record has been removed since the dataset itself is sufficient.

## Data
The source of this data is the 1994 census data available on UCI.
https://archive.ics.uci.edu/static/public/2/adult.zip

## Instructions

#### Downloading data
If you're on a linux os, run the below commands to download data.
1. data="https://archive.ics.uci.edu/static/public/2/adult.zip"
2. wget $data
3. sudo apt-get install unzip
4. unzip -d data/ adult.zip
5. Ensure data is present within the `/data` folder

#### How to run training
1. Clone the repository
2. Navigate to the project folder and open a new terminal
3. Run `pip install pipenv`
4. Run `pipenv install --python 3.10`
5. Activate shell using `pipenv shell`
6. Once inside the shell run `python training.py`

#### How to run prediction service in local
1. Navigate to the project folder and open a new terminal
2. Activate shell using `pipenv shell`
3. Once inside the shell run `python predict.py`
4. The prediction service is now available on `http://localhost:9696`. You can test it using `predict-test.py` (Note - Don't forget the update the URL in the file)

#### How to build and run container for prediction service
1. Navigate to the project folder and open a new terminal
2. If you have docker installed
    1. Run `docker build -t high-income-prediction:latest .` to create the container image.
    2. Run `docker container run -p 9696:9696 <image-id>`
3. The prediction service is now available on `http://localhost:9696`. You can test it using `predict-test.py` (Note - Don't forget the update the URL in the file)

## Deployment
The prediction web service is deployed using Google cloud run and is available at - `https://high-income-prediction-image-mj4wgddl6q-uc.a.run.app/predict`

Here is a sample JSON you can use to test it - 
```json
{
    "workclass": "state_gov", 
    "education": "bachelors", 
    "marital_status": "never_married", 
    "occupation": "adm_clerical", 
    "relationship": "not_in_family", 
    "race": "white", 
    "sex": "male", 
    "native_country": "united_states", 
    "age": 39, 
    "capital_gain": 2174, 
    "capital_loss": 0, 
    "hours_per_week": 40
}
```
You can acces it either using -
- `predict-test.py` (Note - Don't forget the update the URL in the file)
or
- Postman application as shown in the image below -

![alt text](https://github.com/Shubh18s/high-income-earner-prediction/blob/6385ba9d20b63529fe17fedf6144c1ec6a15bdf4/high-income-earner-web-service-screenshot.png)

The video demonstrating the deployed webservice can be found here - https://vimeo.com/manage/videos/881664892

#### Instructions to deploy on Cloud Run
1. Create a service account with Admin role for Cloud Build and make sure the service account has Admin role to Cloud Run.
2. While in the project directory, run - `gcloud builds submit --config cloudbuild.yaml` using the cloud build service account. This should build and deploy the image as a service on Cloud Run.
3. If for some reason the Cloud Run step fails, you can use the Google Cloud UI to directly deploy the image from Container Registry to Cloud Run as well.

## Contributors
singh18shubhdeep@gmail.com