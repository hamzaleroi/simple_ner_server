FROM --platform=linux/amd64 mysql:8.0.26

ARG MYSQL_USER
ARG MYSQL_PASSWORD
RUN  apt-get update && apt-get install -y python3-pymysql
CMD ["--default-authentication-plugin=mysql_native_password"]
