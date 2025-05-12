FROM python:3.13-slim

WORKDIR /app
ENV PYTHONUNBUFFERED 1

COPY requirements.txt pyproject.toml setup.py /app/
RUN pip3 install --no-cache-dir .

COPY . /app

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]