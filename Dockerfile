FROM python:3.8
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN python manage.py db upgrade
CMD python app.py
