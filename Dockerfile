FROM python:3.8-slim-bullseye

RUN apt-get update -y && apt-get install -y awscli

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["bash", "-c", "python main.py && python app.py"]