#!/bin/bash 

set -x -e 

set -x -e

sudo su - ec2-user

sudo yum update -y

sudo yum install git -y

cd /home/ec2-user
git clone https://github.com/awsbigdata/awsathenalab.git


