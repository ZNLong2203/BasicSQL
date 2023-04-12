import requests
import json
import pymysql
import pandas as pd

# Define the API URL and parameters
url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

# Send a GET request to the API
response = requests.get(url)

# Check the status code
if response.status_code == 200:
    # Extract the raw data from the response
    data = response.json()

    json_data = json.dumps(data, indent=4)
    with open("raw.json", "w") as f:
        f.write(json_data)

    # Remove the source key from the json object
    json_obj = json.loads(json_data)
    del json_obj['source']

    # Create a pandas DataFrame from the data
    json_data = json.dumps(json_obj, indent=4)
    df = pd.read_json(json_data)
    df.reset_index(drop=True, inplace=True)
    with open("data.json", "w") as f:
        f.write(df.to_string())  

    # Connect to the database
    cnt = pymysql.connect(host="localhost", user="root", password="", db="json")
    cursor = cnt.cursor()
else:
    print(response)
