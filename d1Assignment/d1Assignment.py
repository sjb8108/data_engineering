import json
import boto3
import d1Assignment.key as key
import os
import time

def main():
    client = boto3.client("kinesis", aws_access_key_id=key.AWS_SESSION, aws_secret_access_key=key.AWS_KEY, region_name='us-east-2')
    directoryOfJSONS = r"C:\\Users\\Scott\\Documents\\data_engineering\\d1Assignment\\InjectedFiles"
    for filename in os.listdir(directoryOfJSONS):
        with open(os.path.join(directoryOfJSONS, filename)) as f:
            data = json.load(f)
        response = client.put_record(StreamName="D1-Assignment-Megazone", Data=json.dumps(data), PartitionKey="1")
        print(response)
    
if __name__ == "__main__":
    main()