FROM ubuntu:latest

ARG DEBIAN_FRONTED=noninteractive


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \ 
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /worksapce

COPY saludo.proto server.py client.py *.jpg ./

RUN git clone https://github.com/Spacee44/SDD_DockerFiles.git

#HACER REPO
CMD ["sleep", "infinity"] 
#CMD ["python3", "RCDD/main.py"]