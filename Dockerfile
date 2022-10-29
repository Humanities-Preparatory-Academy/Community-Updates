FROM python:3.9.6-alpine

# set work directory
RUN mkdir -p /app
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /app

RUN pwd
RUN ls /app

WORKDIR /app/community

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]