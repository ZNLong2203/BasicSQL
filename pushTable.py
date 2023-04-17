import requests
import json
import mysql.connector
import numpy as np
import pandas as pd

with open("data.json", "r") as f:
    json_data = json.load(f)

#Connect to the database
cnx = mysql.connector.connect(host="localhost", user="root", password="ngoclong2232003", db="test")
cursor = cnx.cursor()

# Iterate through the data and insert it into the MySQL database
for item in json_data:
    IDNation = item.get("IDNation")
    Nation = item.get("Nation")
    IDYear = item.get("IDYear")
    Year = item.get("Year")
    Population = item.get("Population")
    SlugNation = item.get("SlugNation")
    cursor.execute("INSERT INTO Test (IDNation, Nation , IDYear, Year, Population, SlugNation) VALUES (%s, %s, %s, %s, %s, %s)", (IDNation, Nation, IDYear, Year, Population, SlugNation))


# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()
