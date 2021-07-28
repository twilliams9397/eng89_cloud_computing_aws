# Python boto3 with AWS and S3
- python package boto3 can help connect with s3
- launch new ec2 instance (see README for instructions), for security groups only need port 22 access from local host ip

### boto3 setup
- run following commands to ensure python 3.6 or above is installed, and then install the AWS CLI:
```linux
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
apt list | grep python3.9
sudo apt-get install python3.9
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
sudo update-alternatives --config python3
alias python=python3
sudo apt install python3.9-distutils
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
sudo python3.9 -m pip install awscli (use which ever python version you have installed here, must be 3.6 or above)
aws configure (this step is where AWS access keys are entered and the region is chosen - use same region as instance, eu-west-1 in this case)
```
- to install the boto3 package run ` sudo pip install boto3`
- within the ec2 instance create .py files using the `sudo nano` function, and write any python functionality within them, ensuring the correct imports are in each file
- a file can be created for each separate s3 buket function - create bucket, upload/download files, delete files from bucket, delete bucket:

### .py to create a bucket
```python
import boto3
import logging
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

bucket_name = input("Enter the bucket name:  ")
bucket_region = input("Enter the region for the bucket:  ")
create_bucket(bucket_name, bucket_region)
```
### .py to list buckets
```python
import boto3

s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
```
### .py to upload files
```python
import boto3
import logging
from botocore.exceptions import ClientError

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

file_name = input("What is the name (and extension) of the file?  ")
bucket_name = input("What bucket are you uploading to?  ")

upload_file(file_name, bucket_name)
```
### .py to download files
```python
import boto3

s3 = boto3.client('s3')
bucket_name = input("What bucket are you downloading from?  ")
object_name = input("What is the object name to download?  ")
local_name = input("Choose a name for the local file download:  ")


s3.download_file(bucket_name, object_name, local_name)
```
### .py to delete files/objects
```python
import boto3

s3 = boto3.client('s3')
bucket_name = input("What bucket are you deleting from?  ")
file_name = input("What file are you deleting?  ")

s3.delete_object(Bucket=bucket_name, Key=file_name)

```
### .py to delete buckets (must be empty)
```python
import boto3

s3 = boto3.client('s3')
bucket_name = input("What bucket are you deleting?  ")

s3.delete_bucket(Bucket=bucket_name)
```

- more boto3 s3 commands can be found at https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#id221
