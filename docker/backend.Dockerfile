FROM python:3.9.6

RUN mkdir /source
WORKDIR /source

RUN pip install --upgrade pip
COPY ./source/requirements.txt /source/
RUN pip3 install -r requirements.txt

COPY ./source/start.sh /source/
RUN chmod +x start.sh
ENTRYPOINT ["/source/start.sh"]
