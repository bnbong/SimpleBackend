FROM python:3.10.10

# Setup working directory
WORKDIR /app
COPY . /app

# Runners
RUN pip install --no-cache-dir -r requirements.txt
ENV TZ=Asia/Seoul