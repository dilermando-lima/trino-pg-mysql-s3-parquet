import boto3

s3_client = boto3.client(
    "s3",
    endpoint_url=f"http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)


try:

    s3_client.create_bucket(Bucket="bucket1")
    # trino requires at least one folder into bucket
    s3_client.put_object(Bucket="bucket1", Key="trino/")

except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'BucketAlreadyOwnedByYou' or error_code == 'BucketAlreadyExists':
        print(f"Bucket '{bucket_name}' already exists")
    else:
        raise

