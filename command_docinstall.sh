#!/usr/bin/ksh

docker build --no-cache --tag image_docker .
docker run -it image_docker
docker rm `docker ps -a -q`
echo "y" | sudo -S docker image prune --all
echo "y" | sudo -S docker system prune -a
sudo yum clean all
rm -rf /var/cache/yum
sudo yum remove -y docker-ce docker-ce-cli
sudo yum --disablerepo=docker-ce-edge
sudo yum --disablerepo=docker-ce-test
