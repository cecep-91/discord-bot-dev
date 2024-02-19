FROM python:latest

RUN mkdir /app/
RUN mkdir /secret/
COPY bot.py /secret/
WORKDIR /app/

COPY . .
RUN pip install -r requirements.txt
CMD ["python3","bot.py"]
