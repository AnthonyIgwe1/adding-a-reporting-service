import logging
import boto3
from botocore.exceptions import ClientError

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create an Amazon S3 client with optional region specification
s3_client = boto3.client('s3', region_name='us-west-2')  # Replace 'us-west-2' with your S3 bucket's region if necessary

# Function to generate a presigned URL for downloading an object from an S3 bucket
def generate_presigned_url(bucket_name, object_name, expiration_in_seconds):
    try:
        # Generate a presigned URL for the specified Amazon S3 object
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration_in_seconds,
            HttpMethod='GET'
        )
        logging.info(f"Presigned URL generated successfully for bucket '{bucket_name}' and object '{object_name}'.")
        return {'presigned_url_str': presigned_url}
    except ClientError as e:
        logging.error(f"Error generating presigned URL: {e.response['Error']['Code']} - {e.response['Error']['Message']}")
        return None

# Lambda function handler
def lambda_handler(event, context):
    bucket_name = "images-363548493921-20241107"  # Ensure this is just the bucket name without URL
    object_name = "report.html"
    expiration_in_seconds = 300  # URL expires in 300 seconds (5 minutes)

    # Generate the presigned URL
    response = generate_presigned_url(bucket_name, object_name, expiration_in_seconds)
    
    if response:
        logging.info("Presigned URL generation completed.")
    else:
        logging.error("Failed to generate presigned URL.")
    
    return response

# Example invocation for local testing (not applicable in AWS Lambda)
if __name__ == "__main__":
    # Simulate an event and context for local testing
    test_event = {}
    test_context = {}
    print(lambda_handler(test_event, test_context))
