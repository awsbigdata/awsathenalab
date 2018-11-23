#!/bin/bash

set -x -e


#cd /home/ec2-user/awsathenalab

region=$(curl http://169.254.169.254/latest/dynamic/instance-identity/document|grep region|awk -F\" '{print $4}')

echo "region :  $region"

mkdir -p ~/.aws/

echo "[default]" > ~/.aws/config
echo "region = ${region}" >> ~/.aws/config

RUN ln -sf /dev/stdout /var/log/athenalab.log \
    && ln -sf /dev/stderr /var/log/athenalaberror.log

pip install -r requirements.txt

python dummy.py password

python mockdataCreation.py

nohup python app.py >server.log

echo "server started"
