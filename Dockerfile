FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    wget \
    python3.6 \
    python3-pip \
    allure \
    npm \
    default-jre

RUN npm install -g allure-commandline --save-dev


COPY ./ /

WORKDIR ./tests

RUN chmod +x start.sh

RUN pip3 install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt

CMD ["./start.sh"]