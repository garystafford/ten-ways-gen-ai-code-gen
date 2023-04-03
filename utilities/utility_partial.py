# write a script calculates the total size of an Amazon S3 bucket using the boto3 library and the list_objects_v2 operation

import argparse
import boto3
import botocore


def get_s3_bucket_size(bucket_name):
    