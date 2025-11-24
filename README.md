D0: Actual Submission
How to Run:

D1: This was done for fun and messing around with AWS because of this the IaC for this is only the example data injection in the aws firehose since I created everything else from the AWS website. Since D0 is my submission I know now what IaC means now after realzing I should of used AWS CDK in python to create the below applications. Below I will list what configurations I had for all AWS applications used if you want to check my application:\
Note: If a setting/parameter is not listed that means the option was not enabled!
1. Amazon Kinesis\
    &ensp; Name: D1-Assignment-Megazone \
2. Amazon Data Firehose\
    &ensp; Kinesis Data Stream: D1-Assignment-Megazone\
    &ensp; Convert Record Format: True\
    &ensp; Output Format: Apache Parquet\
    &ensp; AWS Glue region: United States (Ohio)\
    &ensp; AWS Glue database: d1assignment\
    &ensp; AWS Glue table: books\
    &ensp; S3 Bucket: s3://d1-megazone\
    &ensp; S3 Bucket Prefix: year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/ \
    &ensp; S3 Bucket Error Output: error/ 
3. Amazon S3\
    &ensp; Bucket Name: d1-megazone
4. AWS Glue Database\
    &ensp; Database Name: d1assignment
5. AWS Glue Tables\
    &ensp; Table Name: books\
    &ensp; Database: d1assignment\
    &ensp; Include path: s3://d1-megazone\
    &ensp;Classification: Parquet\
    &ensp; Schema:\
        &ensp;&ensp; Column 1: \
            &ensp;&ensp;&ensp; Name: ibn\
            &ensp;&ensp;&ensp; Data type: string\
            &ensp;&ensp;&ensp; Parition key: -\
        &ensp;&ensp; Column 2:\
           &ensp;&ensp;&ensp;  Name: title\
            &ensp;&ensp;&ensp; Data type: string\
            &ensp;&ensp;&ensp; Parition key: -\
        &ensp;&ensp; Column 3:\
            &ensp;&ensp;&ensp; Name: publisheddate\
            &ensp;&ensp;&ensp; Data type: string\
            &ensp;&ensp;&ensp; Parition key: -\
        &ensp;&ensp; Column 4:\
            &ensp;&ensp;&ensp; Name: pagecount\
            &ensp;&ensp;&ensp; Data type: int\
            &ensp;&ensp;&ensp; Parition key: -\
        &ensp;&ensp; Column 5:\
            &ensp;&ensp;&ensp; Name: audience\
            &ensp;&ensp;&ensp; Data type: string\
            &ensp;&ensp;&ensp; Parition key: -\
        &ensp;&ensp; Column 6: \
            &ensp;&ensp;&ensp; name: year\
            &ensp;&ensp;&ensp; Data type: string\
            &ensp;&ensp;&ensp; Parition key: Parition(0)\
        &ensp;&ensp; Column 7: \
            &ensp;&ensp;&ensp; Name: month\
            &ensp;&ensp;&ensp; Data type: string\
            &ensp;&ensp;&ensp; Parition key: Parition(1)\
        &ensp;&ensp; Column 8: \
            &ensp;&ensp;&ensp; Name: day\
            &ensp;&ensp;&ensp; Data type: string\
            &ensp;&ensp;&ensp; Parition key: Parition(2)
6. Amazon Athena\
    &ensp; Athena Sample Queries:\
        &ensp;&ensp; SELECT * FROM "AwsDataCatalog"."d1assignment"."books" limit 10;\
        &ensp;&ensp; SELECT title FROM "AwsDataCatalog"."d1assignment"."books" limit 5;\
        &ensp;&ensp; SELECT ibn FROM "AwsDataCatalog"."d1assignment"."books" WHERE audience = 'kids'