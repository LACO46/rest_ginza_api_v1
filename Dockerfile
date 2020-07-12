FROM python:3.7.5

RUN pip install --upgrade pip

ADD requirements.txt /
RUN pip install -r requirements.txt