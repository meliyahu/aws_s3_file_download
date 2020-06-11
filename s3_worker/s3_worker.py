import boto3, botostubs
from botocore.client import ClientError
import logging
import argparse
import os
import time
from config import Config
import sys 


class S3Worker():
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.check_creds()
        self.s3_client = boto3.client('s3', aws_access_key_id=Config.AWS_ACCESS_KEY_ID , aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY) # type: botostubs.S3
    
    def check_creds(self):
        if Config.AWS_ACCESS_KEY_ID is None or Config.AWS_SECRET_ACCESS_KEY is None:
            sys.exit("Error: AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY missing! Please pass them as environment variables!")
            
    def execute(self):
        
        # Todo check if bucket exists
        error, bucket_exist = self.does_bucket_exist()
        if bucket_exist == False:
            logging.error(f'Bucket [{self.bucket_name}] does not exist in AWS S3! {error}')
            print()
            sys.exit(f"Bucket {self.bucket_name} does not exists in AWS S3! {error}")
        
        last_added_file = self.get_latest_s3_file()
        if last_added_file is None:
            logging.error(f'There are no files in bucket [{self.bucket_name}]!')
            print()
            sys.exit(f"There are no files in bucket [{self.bucket_name}]!")
        
        download_file = os.path.join(Config.DOWNLOADS_FOLDER, last_added_file)
           
        with open(download_file, 'wb') as f:
            self.s3_client.download_fileobj(self.bucket_name, last_added_file, f)
            logging.info(f'File {last_added_file} was downloaded from AWS S3 bucket successfully!')
            print()
            print(f'File {last_added_file} was download from AWS S3 bucket successfully!')
            print()
            
            
    def get_latest_s3_file(self): 
        """
         Get the latest file in the buckect
        """
        get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
        
        paginator = self.s3_client.get_paginator('list_objects')
        page_iterator = paginator.paginate(Bucket=self.bucket_name)
        last_added = None
        for page in page_iterator:
            # print(f'page: {page["Contents"]}')
            if "Contents" in page:
                last_added = [obj['Key'] for obj in sorted(page["Contents"], key=get_last_modified)][-1]
        
        return last_added  
    
    def does_bucket_exist(self):
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
            return None, True
        except ClientError as err:
            return err, False  
    
    