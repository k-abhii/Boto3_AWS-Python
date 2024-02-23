import boto3
import sys
print(sys.version)


# Create an S3 resource
s3 = boto3.resource('s3')

# Iterate through all buckets and print their names
for bucket in s3.buckets.all():
    print(bucket.name)
