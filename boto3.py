import boto3

# use Amazon s3
s3 = boto3.resource('s3')

# create an Amazon s3 bucket

# create and upload a file
test = open("test.txt", "w")
test.write("test file for boto3 package")
test.close()