# awsathenalab
awsathenalab in python

#Build start
service docker start
docker build  --build-arg AWS_DEFAULT_REGION=us-east-1 . --no-cache
docker run -d -p 80:4000 athenalab

##Stop

docker ps -a
docker stop <id>
