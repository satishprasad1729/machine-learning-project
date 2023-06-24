FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# Adjust the port based on the port your app listens to in Cyclic.sh
EXPOSE 8080
CMD gunicorn --workers=4 --bind 0.0.0.0:8080 app:app