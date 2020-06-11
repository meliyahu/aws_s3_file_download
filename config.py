import os
import sys

class Config:
  
    # Not used  
    S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME', 'tern_ausplots_uploads')
    # Not used
    S3_OBJECT_NAME = os.environ.get('S3_OBJECT_NAME', 'ausplots_db_dump.dump')

    # Set env var for access_key_id and screte_access_key
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '') 
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')

    ROOT_DIR = os.path.abspath(os.curdir)
    
    # Download folder
    DOWNLOADS_FOLDER = os.path.join(ROOT_DIR, 'downloads')  