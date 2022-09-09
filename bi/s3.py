import os

import boto3, botocore

def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3',
                             aws_access_key_id='',
                             aws_secret_access_key ='',
                             )
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response
