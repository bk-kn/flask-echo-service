FROM python:3.10.4-slim-bullseye

WORKDIR /app/py-echo
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/py-echo/

WORKDIR /app/py-echo/src
CMD ["flask", "run", "--host=0.0.0.0"]