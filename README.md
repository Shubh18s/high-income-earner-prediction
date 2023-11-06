# High income earner prediction
The project predicts high income (>$50k/yr.) earners from 1994 census data.

# data
The source of this data is the 1994 census data available on UCI.
https://archive.ics.uci.edu/static/public/2/adult.zip

# Task
Based on the attributes of an individual such as age, education,
marital-status, occupation, race etc. we try to predict whether they earn over $50k/year. 

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

#### How to build the container image for prediction service
1. Navigate to the project folder and open a new terminal
2. If you have docker installed
    1. Run `docker build -t high-income-prediction:latest .` to create the container image.
    2. Run `docker container run -p 9696:9696 <image-id>`
3. The prediction service is now available on `http://localhost:9696`. You can test it using `predict-test.py` (Note - Don't forget the update the URL in the file)