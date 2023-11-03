FROM python:3.9.6
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /src/app
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin python3-gdal
    
WORKDIR /src/app
COPY . src/app
COPY requirements.txt /src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
