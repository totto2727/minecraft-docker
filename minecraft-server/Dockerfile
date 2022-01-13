FROM openjdk:17-bullseye

RUN apt update -y && apt upgrade &&\
    mkdir /opt/minecraft-server

WORKDIR /opt/minecraft-server

RUN curl -o forge-installer.jar -L https://maven.minecraftforge.net/net/minecraftforge/forge/1.18.1-39.0.19/forge-1.18.1-39.0.19-installer.jar &&\
    java -jar forge-installer.jar --installServer &&\
    echo eula=true > eula.txt

CMD [ "./run.sh" ]