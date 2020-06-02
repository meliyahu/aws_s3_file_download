import os
import sys

class Config:
    
    S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME', 'tern_ausplots_uploads')
    S3_OBJECT_NAME = os.environ.get('S3_OBJECT_NAME', 'ausplots_db_dump.dump')

    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'my_aws_access_key_id') 
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', 'my_aws_secrete_access')
     