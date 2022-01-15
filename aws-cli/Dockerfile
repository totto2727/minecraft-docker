FROM amazon/aws-cli

COPY ./scripts /opt/scripts

RUN yum install -y zip &&\
    chmod 111 /opt/scripts/* &&\
    amazon-linux-extras install -y python3.8 &&\
    echo 'alias python=python3.8' >> ~/.bashrc &&\
    echo 'alias pip=pip3.8' >> ~/.bashrc

ENTRYPOINT /opt/scripts/launch.sh && /bin/bash
# ENTRYPOINT /bin/bash