from ubuntu:latest

RUN DEBIAN_FRONTEND="noninteractive" apt update
RUN DEBIAN_FRONTEND="noninteractive" apt install -y python3-pip
RUN DEBIAN_FRONTEND="noninteractive" pip install flask

workdir /project