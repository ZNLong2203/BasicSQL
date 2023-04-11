import requests
import json
import pandas as pd

# Define the API URL and parameters
url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

# Send a GET request to the API
response = requests.get(url)

# Check the status code
if response.status_code == 200:
    # Extract the data from the response
    data = response.json()

    json_data = json.dumps(data, indent=4)

    json_obj = json.loads(json_data)

    del json_obj['source']

    json_data = json.dumps(json_obj, indent=4)

    with open("data.json", "w") as f:
        f.write(json_data)

    # Create a pandas DataFrame from the data
    df = pd.read_json('data.json')
    print(df.to_string())  
else:
    print(response)
