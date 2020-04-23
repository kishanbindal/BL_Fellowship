import boto3
from botocore.client import Config
import os
import dotenv
import logging

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(base_path, '..env')
dotenv.load_dotenv(env_path)


class AmazonServicesS3Util:

    s3_signature = {
        'v4': 's3v4',
        'v2': 's3'
    }

    @staticmethod
    def create_s3_client():
        s3 = boto3.client('s3')
        return s3

    @staticmethod
    def generate_url(key):
        url = f"https://{os.getenv('AWS_STORAGE_BUCKET_NAME')}.s3.ap-south.amazonaws.com/{key}"
        return url

    @staticmethod
    def upload_image_file(s3_client, image_file, key):
        s3_client.upload_fileobj(image_file, os.getenv('AWS_STORAGE_BUCKET_NAME'), key)

    @staticmethod
    def generate_presigned_url(bucket_key, bucket_name=os.getenv('AWS_STORAGE_BUCKET_NAME'), expiration=3600,
                               signature_version=s3_signature['v4']):

        s3_client = boto3.client('s3',
                                 region_name='ap-south-1',
                                 config=Config(signature_version='s3v4'))

        presign_url = s3_client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': bucket_key
            },
            ExpiresIn=expiration
        )
        return presign_url
