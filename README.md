# high-income-earner-prediction
The project predicts high income (>$50k/yr.) earners from 1994 census data.

# data
The source of this data is the 1994 census data available on UCI.
https://archive.ics.uci.edu/static/public/2/adult.zip

# Task
Based on the attributes of an individual such as age, education,
marital-status, occupation, race etc. we try to predict whether they earn over $50k/year. 

#### Downloading data
` If you're on a linux os, run the below commands to download data. `
- 1. data="https://archive.ics.uci.edu/static/public/2/adult.zip"
- 2. wget $data
- 2. sudo apt-get install unzip
- 3. unzip -d data/ adult.zip