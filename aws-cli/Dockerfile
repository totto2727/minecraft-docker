FROM amazon/aws-cli

COPY ./scripts /opt/scripts

RUN yum install -y zip && chmod 111 /opt/scripts/*

ENTRYPOINT [ "/opt/scripts/launch.sh" ]