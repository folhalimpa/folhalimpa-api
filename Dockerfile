FROM ubuntu

RUN echo "deb http://ftp.de.debian.org/debian experimental main\n" >> /etc/apt/sources.list \
 && echo "deb http://ftp.de.debian.org/debian unstable main\n" >> /etc/apt/sources.list

RUN apt-get update \
 && apt-get install -y --allow-unauthenticated python3.6 python3-pip

COPY . /fl-api

RUN pip3 install -r /fl-api/requirements.txt

EXPOSE 8000

WORKDIR /fl-api

CMD python3 api/manage.py runserver 0.0.0.0:8000