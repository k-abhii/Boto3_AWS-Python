import boto3
import os


def create_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} created successfully.")


def upload_file(bucket_name, local_file_path, s3_object_key):
    s3 = boto3.client('s3')
    s3.upload_file(local_file_path, bucket_name, s3_object_key)
    print(f"File uploaded to {s3_object_key} in {bucket_name} successfully.")


def download_file(bucket_name, s3_object_key, local_destination_path):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, s3_object_key, local_destination_path)
    print(f"File downloaded from {s3_object_key} in {bucket_name} successfully.")


def delete_file(bucket_name, s3_object_key):
    s3 = boto3.client('s3')
    s3.delete_object(Bucket=bucket_name, Key=s3_object_key)
    print(f"File {s3_object_key} deleted from {bucket_name} successfully.")


def delete_bucket(bucket_name):
    s3 = boto3.client('s3')

    # Before deleting the bucket, make sure it's empty
    bucket_objects = s3.list_objects(Bucket=bucket_name).get('Contents', [])
    for obj in bucket_objects:
        s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

    # Now, delete the bucket
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} deleted successfully.")


if __name__ == "__main__":
    # Replace with your own values
    my_bucket_name = '8298845-abhimanyu-create-bucket-1'
    local_file_path = 'C:\\Users\\hp\\PycharmProjects\\Boto_aws_python\\Boto_aws_python\\my_local_download.txt'
    s3_object_key = 'your-s3-object-key'
    local_destination_path = 'abhi.txt'

    # Create bucket
    create_bucket(my_bucket_name)

    # Upload file to bucket
    upload_file(my_bucket_name, local_file_path, s3_object_key)

    # Download file from bucket
    download_file(my_bucket_name, s3_object_key, local_destination_path)

    # Delete file from bucket
    delete_file(my_bucket_name, s3_object_key)

    # Delete bucket
    delete_bucket(my_bucket_name)
