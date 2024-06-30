FROM python:3.11.1

WORKDIR /app

ADD databaseFuntions.py .
ADD app.py .
ADD requirements.txt .


RUN pip install -r requirements.txt

CMD ["python", "./app.py"]