FROM ubuntu:18.04
LABEL Maintainer="Mohammed Ashour <github.com/Mohammed-Ashour>"

RUN apt update -y && apt upgrade -y &&\
    apt install wget -y &&\
    wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz &&\
    tar -xvzf geckodriver* &&\
    chmod +x geckodriver &&\
    mv -f geckodriver /usr/local/share/geckodriver &&\
    ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver &&\
    ln -s /usr/local/share/geckodriver /usr/bin/geckodriver

#installing python3.7
RUN apt install software-properties-common -y &&\
    add-apt-repository ppa:deadsnakes/ppa &&\
    apt install python3.7 -y

RUN apt install python3-pip -y
#cloning the repo 
RUN apt-get install git -y &&\
    git clone https://github.com/OWASP/QRLJacking &&\
    python3.7 -m pip install pip &&\
    python3.7 -m pip install -r QRLJacking/QRLJacker/requirements.txt

ENTRYPOINT [ "bash" ]


