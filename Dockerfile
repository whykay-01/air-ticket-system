FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD [ "flask", "--app", "flask_app", "run", "--host=0.0.0.0", "--port=8000", "--debug" ]