FROM python:3.9.1
RUN apt-get update
RUN apt-get -y install tesseract-ocr
RUN apt-get install tesseract-ocr-spa
ADD . /sweet-teacher-aid
WORKDIR /sweet-teacher-aid
RUN pip install -r requirements.txt