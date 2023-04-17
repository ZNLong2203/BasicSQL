import requests
import json
import mysql.connector
import numpy as np
import pandas as pd

# Define the API URL and parameters
url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

# Send a GET request to the API
response = requests.get(url)

# Check the status code
if response.status_code == 200:
    # Raw data from the response
    data = response.json()

    json_data = json.dumps(data)
    with open("raw.json", "w") as f:
        f.write(json_data)

    # Remove the source key from the json object
    json_obj = json.loads(json_data)
    del json_obj['source']

    # Create a pandas DataFrame from the data
    json_data = json.dumps(json_obj, indent=4)
    df = pd.read_json(json_data)
    df = pd.DataFrame(df["data"].to_list())
    df = df.rename(columns={"ID Nation": "IDNation"})
    df = df.rename(columns={"ID Year": "IDYear"})
    df = df.rename(columns={"Slug Nation": "SlugNation"})
    df.to_json("data.json", orient="records", indent=4)
    
else:
    print(response)
