import boto3
import botocore
import os

from dotenv import load_dotenv

def s3_client():

    load_dotenv()
    session = boto3.session.Session()

    client = session.client('s3',
                    config=botocore.config.Config(s3={'addressing_style': 'virtual'}),
                    region_name='nyc3',
                    endpoint_url='https://nyc3.digitaloceanspaces.com',
                    aws_access_key_id=os.getenv('DIGITAL_OCEAN_SPACES_ID'),
                    aws_secret_access_key=os.getenv('DIGITAL_OCEAN_SPACES_SECRET_KEY')
                )

    return client