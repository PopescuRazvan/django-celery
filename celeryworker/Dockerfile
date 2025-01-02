FROM python:3.11.4-alpine

WORKDIR /usr/src/app

#prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
#ensure Python outputs everything that's printed inside the application
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

