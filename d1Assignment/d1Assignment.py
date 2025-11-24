import json
import boto3
import d1Assignment.key as key
import os
import time

"""
Connects to client and injects JSON files from a folder to AWS firehose
Parameters: None
Returns: None
"""

def main():
    client = boto3.client("kinesis", aws_access_key_id=key.AWS_SESSION, aws_secret_access_key=key.AWS_KEY, region_name='us-east-2') #connects to client using session and password key
    directoryOfJSONS = r"C:\\Users\\Scott\\Documents\\data_engineering\\d1Assignment\\InjectedFiles"
    for filename in os.listdir(directoryOfJSONS): #loops over entire folder
        with open(os.path.join(directoryOfJSONS, filename)) as f:
            data = json.load(f) #opens each file and data data
        response = client.put_record(StreamName="D1-Assignment-Megazone", Data=json.dumps(data), PartitionKey="1") #send data to data stream called D1-Assignment-Megazone
        print(response)
    
if __name__ == "__main__":
    main()