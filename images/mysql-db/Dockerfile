FROM mysql:latest

COPY images/mysql-db/my.cnf /etc/mysql/conf.d/my.cnf

ENV MYSQL_ROOT_PASSWORD=pass
ENV MYSQL_USER=user
ENV MYSQL_DATABASE=alrdmc

EXPOSE 3306