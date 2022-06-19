FROM --platform=linux/amd64 mysql:8.0.26

ARG MYSQL_USER
ARG MYSQL_PASSWORD
COPY ./dump/dump.sql /tmp

CMD ["mysqld","--default-authentication-plugin=mysql_native_password","--init-file=/tmp/dump.sql"]
