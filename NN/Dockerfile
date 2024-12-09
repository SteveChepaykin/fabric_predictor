FROM python:3.9-slim

WORKDIR /NN

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .

CMD ["python", "network_app.py"]