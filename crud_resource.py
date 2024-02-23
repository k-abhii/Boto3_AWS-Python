import boto3
import os

def create_bucket(bucket_name):
    s3 = boto3.resource('s3')
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} created successfully.")

def upload_file(bucket_name, local_file_path, s3_object_key):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.upload_file(local_file_path, s3_object_key)
    print(f"File uploaded to {s3_object_key} in {bucket_name} successfully.")

def read_and_print_file_content(local_file_path):
    with open(local_file_path, 'r') as file:
        file_content = file.read()
        print(f"Content of the file:\n{file_content}")


def download_file(bucket_name, s3_object_key, local_destination_path):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.download_file(s3_object_key, local_destination_path)
    print(f"File downloaded from {s3_object_key} in {bucket_name} successfully.")


def delete_file(bucket_name, s3_object_key):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, s3_object_key)
    obj.delete()
    print(f"File {s3_object_key} deleted from {bucket_name} successfully.")


def delete_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    # Delete all objects in the bucket
    bucket.objects.all().delete()

    # Now, delete the bucket
    bucket.delete()
    print(f"Bucket {bucket_name} deleted successfully.")

def list_buckets():
    s3 = boto3.resource('s3')
    buckets = [bucket.name for bucket in s3.buckets.all()]
    print("Available Buckets:")
    for bucket in buckets:
        print(bucket)

if __name__ == "__main__":
    # Replace with your own values
    my_bucket_name = '12345-abhimanyu-new-bucket'
    local_file_path = 'C:\\Users\\hp\\PycharmProjects\\Boto_aws_python\\Boto_aws_python\\my_local_download.txt'
    s3_object_key = 'your-s3-object-key'
    local_destination_path = 'file.txt'

    # Create bucket
    create_bucket(my_bucket_name)

    # Read and print file content
    read_and_print_file_content(local_file_path)

    # Upload file to bucket
    upload_file(my_bucket_name, local_file_path, s3_object_key)

    # Download file from bucket
    download_file(my_bucket_name, s3_object_key, local_destination_path)

    # Delete file from bucket
    delete_file(my_bucket_name, s3_object_key)

    # Delete bucket
    delete_bucket(my_bucket_name)

    # List all available buckets
    list_buckets()


# C:\Python38\python.exe C:\Users\hp\PycharmProjects\Boto_aws_python\Boto_aws_python\crud_resource.py
# Bucket 12345-abhimanyu-new-bucket created successfully.
# Content of the file:
# This is a text file for upload
#
# git remote add origin https://github.com/k-abhii/Boto3_AWS-Python.git
# git branch -M main
# git push -u origin main
# File uploaded to your-s3-object-key in 12345-abhimanyu-new-bucket successfully.
# File downloaded from your-s3-object-key in 12345-abhimanyu-new-bucket successfully.
# File your-s3-object-key deleted from 12345-abhimanyu-new-bucket successfully.
# Bucket 12345-abhimanyu-new-bucket deleted successfully.
# Available Buckets:
# 829-my-first-bucket-test
#
# Process finished with exit code 0
