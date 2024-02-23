import boto3
client = boto3.client('s3')
# client.create_bucket(Bucket='8298845885-my-first-bucket-test')

# # with open('myfile.txt','w') as file:
#     file.write('This is a text file for upload')
# client.upload_file(Filename='myfile.txt',Bucket='8298845885-my-first-bucket-test',Key='test-upload-file')
# client.download_file(Bucket='8298845885-my-first-bucket-test',Key='test-upload-file',Filename='my_local_download.txt')


# with open('my_local_download.txt','r') as f:
#     print(f.read())

# client.delete_object(Bucket='8298845885-my-first-bucket-test',Key='test-upload-file')
# client.download_file(Bucket='8298845885-my-first-bucket-test',Key='test-upload-file',Filename='my_local_download.txt')
