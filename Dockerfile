FROM python:3.7.5

RUN pip install --upgrade pip

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD app/user_dict/sudachi.json /
RUN cp sudachi.json /usr/local/lib/python3.7/site-packages/sudachipy/resources/sudachi.json