FROM python:3.13-slim

WORKDIR /app
ENV PYTHONUNBUFFERED 1

# Copia os arquivos necessários para o pip resolver o '-e .'
COPY requirements.txt setup.py /app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]