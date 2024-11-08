FROM mysql:latest

COPY images/mysql-db/my.cnf /etc/mysql/conf.d/my.cnf

ENV MYSQL_ROOT_PASSWORD=pass
ENV MYSQL_USER=root
ENV MYSQL_DATABASE=alrdmc

EXPOSE 3306