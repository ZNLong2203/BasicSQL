import requests
import json
import mysql.connector
import numpy as np
import pandas as pd

#Connect to the database
cnx = mysql.connector.connect(host="localhost", user="root", password="ngoclong2232003", db="test")
cursor = cnx.cursor()

# Define the SQL query to create a table
sql = "CREATE TABLE Test (ID INT AUTO_INCREMENT PRIMARY KEY, IDNation VARCHAR(255), Nation VARCHAR(255), IDYear INT, Year VARCHAR(255), Population INT, SlugNation VARCHAR(255))"

# Execute the query to create the table
cursor.execute(sql)

# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()
print("Table 'Test' created.")
