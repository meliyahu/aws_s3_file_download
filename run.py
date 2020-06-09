import logging
import argparse
import os

from s3_worker import S3Worker

def run(s3_bucket_name: str):
    logging.basicConfig(level=logging.INFO,
                        filename=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs', 'output.log'),
                        filemode='w',
                        format='%(asctime)s %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S %p')

    downloader = S3Worker(s3_bucket_name)
    downloader.execute()
    
    
def cli():
    parser = argparse.ArgumentParser(description='AWS S3 File downloader')
    parser.add_argument('--s3_bucket_name', action="store", required=True, help='S3_BUCKET_NAME the bucket(container) is S3 where the item is stored')
    return parser.parse_args()


def main(args):
    run(args.s3_bucket_name)


if __name__ == '__main__':
    args = cli()
    main(args)