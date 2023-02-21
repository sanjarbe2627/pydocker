FROM python:3.8

WORKDIR projects/pydocker

COPY main.py ./
COPY .gitignore ./
COPY README.md ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]