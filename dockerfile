# image
FROM ubuntu:bionic

RUN apt-get update && apt-get install -y python3-dev libboost-all-dev git cmake g++ gdb python3-dbg vim libgoogle-glog-dev libgflags-dev swig
RUN apt update && apt install mecab && \
    apt install libmecab-dev && \
    apt install mecab-ipadic-utf8 && \
    apt install python3-pip

RUN pip3 install mecab-python3

# language environment settings
RUN apt-get -y install language-pack-ja-base language-pack-ja

# env var
ENV LANG ja_JP.UTF-8
ENV CPLUS_INCLUDE_PATH="$CPLUS_INCLUDE_PATH:/usr/include/python3.4m/"

WORKDIR /workspace/