#!/bin/bash

set -x -e

sudo su - ec2-user

sudo yum update -y

sudo yum install git -y

git clone https://github.com/awsbigdata/awsathenalab.git

sudo pip install -r requirements.txt 

screen -S pythonserver -L -Logfile pythonserver.log -d -m sudo python app.py

echo "server started"
