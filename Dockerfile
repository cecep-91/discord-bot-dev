FROM python:latest

RUN apt-get update && apt-get install -y procps

RUN mkdir /app/
RUN mkdir /secret/
COPY bot.py /secret/
WORKDIR /app/

COPY . .
RUN pip install -r requirements.txt
CMD ["python3","bot.py"]
