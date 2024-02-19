FROM python:latest

RUN mkdir /app/
WORKDIR /app/

COPY . .
RUN pip install -r requirements.txt
CMD ["python3","bot.py"]
