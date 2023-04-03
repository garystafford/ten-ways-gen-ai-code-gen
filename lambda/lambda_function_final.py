# Purpose: Read a file from S3 and write it to a DynamoDB table
# Author: Gary A. Stafford
# Date: 2023-04-02

# write a lambda function that will read a file from s3
# and write it to a dynamodb table

import boto3
import json
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    s3 = boto3.resource("s3")
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["TABLE_NAME"])
    bucket = s3.Bucket(os.environ["BUCKET_NAME"])

    for obj in bucket.objects.all():
        logger.info(obj.key)
        body = obj.get()["Body"].read()
        data = json.loads(body)

        for item in data:
            logger.info(item)
            table.put_item(Item=item)

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
