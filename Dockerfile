FROM python:alpine3.8
RUN pip install flask
ADD ./app /app
WORKDIR /app
EXPOSE 80
CMD ["python3", "app.py"]
