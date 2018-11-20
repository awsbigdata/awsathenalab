#!/bin/bash

set -x -e 

cd /home/ec2-user/awsathenalab

sudo pip install -r requirements.txt 

screen -S pythonserver -L -d -m  sudo python app.py

echo "server started"
