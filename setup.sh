#/bin/bash

amazon-linux-extras install docker -y
systemctl enable docker
systemctl start docker
mkdir -p ~/.docker/cli-plugins/
curl -SL https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
chmod +x ~/.docker/cli-plugins/docker-compose
groupadd docker
usermod -aG docker $USER
(crontab -l; echo "@reboot cd ${PWD} && docker compose up -d") | crontab -