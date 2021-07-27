# Cloud Computing with AWS
## 2-tier App Deployment
- use one instance for the node app and one for the mongodb
![2-tier](images/2_tier.png)
### node app setup
- set up AWS ec2 instance
- choose correct AMI (Amazon Machine Image)
![AMI](images/ubuntu_box.png)
- choose correct Instance Type (free tiers available)
**image**
- configure instance details
**image**
- leave storage as it is
- name it in tags (Name: follow AWS conventions)
- security group - ips added to allow explicit access
**image**
- scp command to copy app folder form vagrant setup
- install dependencies (look at provision.sh)
- db env variable

### db setup
- same setup but different security group so only app can access
**image**
- install mongo - look at db provision.sh
- mongod.conf file