# write a lambda function that will read a file from s3 and write it to a dynamodb table

import boto3
import json


def lambda_handler(event, context):
    