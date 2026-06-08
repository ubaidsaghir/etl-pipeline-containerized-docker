import boto3
import requests
import pandas as pd
from datetime import datetime
import os

cities = ["Multan","Lahore","Islamabad"]
records = []

for city in cities:
    params = {
        "key": "b91949b8a95b4b52bf7130520262404",
        "q": city
    }
    
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params=params
    )
    
    data = response.json()
    
    row = {
        "city": data["location"]["name"],
        "temp": data["current"]["temp_c"],
        "humidity": data["current"]["humidity"],
        "timestamp": datetime.now()
    }
    
    records.append(row)

df = pd.DataFrame(records)

file_name = "City_Data.csv"
df.to_csv(file_name, index=False)

print("csv created")


s3 = boto3.client(
    's3',
    region_name='us-east-1',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

bucket_name = "docker-project12"

s3.upload_file(
    Filename="City_Data.csv",
    Bucket="docker-project12",
    Key="City_Data.csv"
)

print("File upload to s3")