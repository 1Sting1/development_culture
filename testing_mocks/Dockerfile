FROM python:3.9-slim

WORKDIR /src

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY .. .

EXPOSE 5000

CMD ["python", "src/server.py"]
