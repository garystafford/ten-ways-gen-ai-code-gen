# Purpose: Calculates the total size of an Amazon S3 bucket
# Author: Gary A. Stafford
# Date: 2023-04-02

# write a script calculates the total size of an Amazon S3 bucket
# using the boto3 library and the list_objects_v2 operation

import argparse
import boto3
import botocore


def get_s3_bucket_size(bucket_name):
    """Return the size of the S3 bucket in bytes.

    Args:
        bucket_name (str): Name of the S3 bucket.

    Returns:
        int: Size of the S3 bucket in bytes.

    """

    s3 = boto3.client("s3")
    total_size = 0
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print("The object does not exist.")
        else:
            raise
    else:
        for content in response["Contents"]:
            total_size += content["Size"]
    return total_size


def main():
    parser = argparse.ArgumentParser(description="Get the size of an S3 bucket")
    parser.add_argument("bucket_name", help="Name of the S3 bucket")
    args = parser.parse_args()
    print(get_s3_bucket_size(args.bucket_name))


if __name__ == "__main__":
    main()
