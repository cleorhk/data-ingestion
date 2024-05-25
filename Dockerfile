FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY load_data.py load_data.py
COPY data /app/data

CMD ["python", "load_data.py"]
