FROM python:3.11.1

WORKDIR /app

ADD databaseFuntions.py .
ADD api_endpoints.py .
ADD app.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

ENV PORT 5000

EXPOSE 5000

CMD ["python", "./app.py"]