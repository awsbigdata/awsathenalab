# awsathenalab
awsathenalab in python

Build start

docker build -t athenalab .
docker run -d -p 80:4000 athenalab

##Stop 

docker ps -a
docker stop <id>
