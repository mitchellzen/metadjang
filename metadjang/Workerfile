FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /webapp
WORKDIR /webapp
ADD requirements.txt /webapp/
RUN pip install -r requirements.txt
ADD . /webapp/
RUN adduser --disabled-password --gecos '' myuser
