FROM centos:centos7

RUN yum install -y python-pip
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade bdworkbench
RUN pip install --upgrade python-docker
RUN pip install --upgrade bdworkbench
