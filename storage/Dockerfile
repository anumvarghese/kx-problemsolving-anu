FROM python:3.8

WORKDIR /storage

COPY requirements.txt .
COPY app.py .
COPY dummy.json .
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh
RUN chmod 775 dummy.json 
RUN chmod +x app.py
COPY . /storage

ENV FLASK_APP=app.py FLASK_RUN_HOST=0.0.0.0

#RUN redisurl="http://download.redis.io/redis-stable.tar.gz"
#RUN curl -s -o redis-stable.tar.gz "http://download.redis.io/redis-stable.tar.gz"
#RUN su root
#RUN mkdir -p /usr/local/lib/
#RUN chmod a+w /usr/local/lib/
#RUN tar -C /usr/local/lib/ -xzf redis-stable.tar.gz
#RUN rm redis-stable.tar.gz
#RUN cd /usr/local/lib/redis-stable/ && make && make install
#RUN redis-cli --version
#RUN su root
#RUN mkdir -p /etc/redis/
#COPY 6379.conf /etc/redis/6379.conf
#RUN redis-server /etc/redis/6379.conf

RUN pip install -r requirements.txt

EXPOSE 8081
#ENTRYPOINT ["./docker-entrypoint.sh" ]
ENTRYPOINT ["python"]
CMD ["app.py", "--host", "0.0.0.0"]
