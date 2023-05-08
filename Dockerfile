FROM python:3.10.9-slim-buster

ENV CODE_MODULE=/code/
ENV DAGSTER_HOME=/code/dagster_home

RUN mkdir -p $DAGSTER_HOME
RUN mkdir -p $CODE_MODULE

WORKDIR $CODE_MODULE

ADD requirements.txt .
ADD requirements.dev.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt -r requirements.dev.txt

EXPOSE 3000

CMD ["bash"]