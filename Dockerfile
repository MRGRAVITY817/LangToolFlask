FROM ubuntu:18.04
LABEL AUTHOR mrgravity817@gmail.com

# Change to mirroring server to get more speed
RUN sed -i 's/kr.archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
ADD ./pip.conf /root/.pip/pip.conf

# Essentials
RUN apt-get update \
  && apt-get install -y \
  openjdk-11-jre-headless python3-pip python3-dev \
  && apt-get clean \
  && pip3 install --upgrade pip

COPY ./app /app
WORKDIR /app

# In case if you want to test with Jupyter
RUN pip install -r requirements.txt
RUN pip install jupyterlab

EXPOSE 5000 
ENTRYPOINT ["python3"]
CMD ["server.py"]
