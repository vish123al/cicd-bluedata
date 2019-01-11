FROM centos:centos7

#RUN yum install wget -y
#RUN yum install unzip -y
#RUN wget https://pypi.python.org/packages/e2/a8/09da35b98cd9c6c9d2f32a2906e330e0bb3d0835d5bd08097e5d6816cdbf/bdworkbench-3.2.2.tar.gz
#RUN gunzip bdworkbench-3.2.2.tar.gz
ARG docker_gid=993
RUN addgroup -g $docker_gid docker && addgroup docker docker
RUN yum install -y python-pip # If pip is not already installed.
RUN pip install --upgrade pip # Ignore any python 2.6 warnings for now.
RUN pip install --upgrade setuptools
RUN pip install --upgrade requests
RUN pip install --upgrade argparse
RUN pip install --upgrade bdworkbench
RUN chmod 777 /helloworld-app.wb
RUN ./helloworld-app.wb
