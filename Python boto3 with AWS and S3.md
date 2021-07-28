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
- to install the boto3 package run ` sudo pip install boto3` or `pip3` in the python terminal
- also install the awscli in the python terminal (may need `sudo` and user password) and go through the configuration steps
