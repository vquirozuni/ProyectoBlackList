# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENV FLASK_APP=application.py

EXPOSE 8000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]