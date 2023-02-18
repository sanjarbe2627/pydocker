FROM python:3.8

ADD main.py .

CMD ["python3", "./main.py"]