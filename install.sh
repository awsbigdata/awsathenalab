#!/bin/bash

set -x -e 

cd /home/ec2-user/awsathenalab

region=$(curl http://169.254.169.254/latest/dynamic/instance-identity/document|grep region|awk -F\" '{print $4}')

mkdir -p ~/.aws/

echo "[default]" > ~/.aws/config
echo "region = ${region}" >> ~/.aws/config

sudo pip install -r requirements.txt 

python dummy.py $1

python mockdataCreation.py

screen -S pythonserver -L -d -m  sudo python app.py

echo "server started"
