D0: Actual Submission

D1: This was done for fun and messing around with AWS because of this the IaC for this is only the example data injection in the aws firehose since I created everything else from the AWS website. below I will list what configurations I had for all AWS applications used if you want to check my application:
Note: If a setting/parameter is not listed that means the option was not enabled!
1. Amazon Kinesis
    Name: D1-Assignment-Megazone
    Everything else was default settings
2. Amazon Data Firehose
    Kinesis Data Stream: D1-Assignment-Megazone
    Convert Record Format: True
    Output Format: Apache Parquet
    AWS Glue region: United States (Ohio)
    AWS Glue database: d1assignment
    AWS Glue table: books
    S3 Bucket: s3://d1-megazone
    S3 Bucket Prefix: year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/
    S3 Bucket Error Output: error/
3. Amazon S3
    Bucket Name: d1-megazone
4. AWS Glue Database
    Database Name: d1assignment
5. AWS Glue Tables
    Table Name: books
    Database: d1assignment
    Include path: s3://d1-megazone
    Classification: Parquet
    Schema:
        Column 1: 
            Name: ibn
            Data type: string
            Parition key: -
        Column 2:
            Name: title
            Data type: string
            Parition key: -
        Column 3:
            Name: publisheddate
            Data type: string
            Parition key: -
        Column 4:
            Name: pagecount
            Data type: int
            Parition key: -
        Column 5:
            Name: audience
            Data type: string
            Parition key: -
        Column 6: 
            Name: year
            Data type: string
            Parition key: Parition(0)
        Column 7: 
            Name: month
            Data type: string
            Parition key: Parition(1)
        Column 8: 
            Name: day
            Data type: string
            Parition key: Parition(2)
6. Amazon Athena
    Athena Sample Queries:
        SELECT * FROM "AwsDataCatalog"."d1assignment"."books" limit 10;
        SELECT title FROM "AwsDataCatalog"."d1assignment"."books" limit 5;
        SELECT ibn FROM "AwsDataCatalog"."d1assignment"."books" WHERE audience = 'kids'