# Use an official Python runtime as a parent image
FROM python:3.11-alpine


WORKDIR /app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY app ./ 


EXPOSE 5000


ENV FLASK_APP=main.py


CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
