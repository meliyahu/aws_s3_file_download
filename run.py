import boto3
import logging
import argparse
import os
import time
from config import Config

def get_latest_s3_file(s3_bucket_name, s3_client):
    
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    
    paginator = s3_client.get_paginator('list_objects')
    page_iterator = paginator.paginate(Bucket=s3_bucket_name)
    last_added = None
    for page in page_iterator:
        # print(f'page: {page["Contents"]}')
        if "Contents" in page:
            last_added = [obj['Key'] for obj in sorted(page["Contents"], key=get_last_modified)][-1]
    
    return last_added


def run(s3_bucket_name: str):
    logging.basicConfig(level=logging.INFO,
                        filename=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs', 'output.log'),
                        filemode='w',
                        format='%(asctime)s %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S %p')

    # Todo start the s3 download logic here.
    s3_client = boto3.client('s3', aws_access_key_id=Config.AWS_ACCESS_KEY_ID , aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY)
    last_added_file = get_latest_s3_file(s3_bucket_name, s3_client)
    print(f'last_added_file: {last_added_file}')
    # TODO Download file to download folder.
    


def cli():
    parser = argparse.ArgumentParser(description='AWS S3 File downloader')
    parser.add_argument('--s3_bucket_name', action="store", required=True, help='S3_BUCKET_NAME the bucket(container) is S3 where the item is stored')
    return parser.parse_args()


def main(args):
    run(args.s3_bucket_name)


if __name__ == '__main__':
    args = cli()
    main(args)