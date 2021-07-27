# Cloud Computing with AWS
## 2-tier App Deployment
- use one instance for the node app and one for the mongodb
![2-tier](images/2_tier.png)
- db instance only accessed by app instance
### node app setup
- set up AWS ec2 instance
- choose correct AMI (Amazon Machine Image)
![AMI](images/ubuntu_box.png)
- choose correct Instance Type (free tiers available)
![instance](images/instance.png)
- configure instance details - any not shown below are left as default
![instance details](images/instance_details.png)
- leave storage as it is
- name it in tags, note that the below image is the databse instance, the app would be the same but _app
![db naming key](images/db_naming)
- security group - ips added to allow explicit access
![app security group](images/app_sg)
- scp command to copy app folder form vagrant setup
- install dependencies (look at provision.sh)
- db env variable

### db setup
- same setup but different security group so only app can access by using app ip address
![db security group](images/db_sg)
- install mongo - look at db provision.sh
- mongod.conf file

### running app