FROM  public.ecr.aws/docker/library/alpine:3.14

RUN apk update
RUN apk add py3-pip \
    && pip install --upgrade pip
RUN apk add make automake gcc g++ subversion python3-dev

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENV FLASK_APP=application.py

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]