# High income earner prediction
The project predicts high income (>$50k/yr.) earners from 1994 census data.

# data
The source of this data is the 1994 census data available on UCI.
https://archive.ics.uci.edu/static/public/2/adult.zip

# Task
Based on the attributes of an individual such as age, education,
marital-status, occupation, race etc. we try to predict whether they earn over $50k/year. 

#### Downloading data
` If you're on a linux os, run the below commands to download data. `
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
5. Run `pipenv shell`
6. Once inside the shell run `python training.py`