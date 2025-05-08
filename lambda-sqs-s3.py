import boto3
import urllib.request

from urllib.parse import urlparse



sqs = boto3.client("sqs")
s3 = boto3.client("s3")

# AWS Configuration
sqs_queue_url='https://ap-south-1.queue.amazonaws.com/941646819596/lambda1311'
s3_bucket = 'lambda-s3-1311'  # Optional
download_to_s3 = True

image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1024px-React-icon.svg.png'

def Lambda_file_upload(event,context):
    for record in event['Records']:
        im_url = record['body']
        print(f'sqs url: {im_url}')

    try:
        parsed_url =  urlparse(im_url)
        file_name= parsed_url.path.split('/')[-1]

        # Download image from URL
        response = urllib.request.urlopen(im_url)
        image_data = response.read()


        # Upload to S3
        s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=image_data, ACL='public-read')

        print(f"Uploaded to s3://{BUCKET_NAME}/{filename}")
    except Exception as e:

        print(f"Failed to process message: {e}")
