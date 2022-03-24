import os

import boto3, botocore

def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3',
                             aws_access_key_id='AKIAYGIXF7RWTHF5TFKN',
                             aws_secret_access_key ='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',
                             )
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response
