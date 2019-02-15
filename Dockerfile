FROM python:3.7

RUN apt-get update && apt-get install -y --no-install-recommends mysql-client
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["bash", "sleep 200"]
