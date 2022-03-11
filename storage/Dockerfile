FROM python:3.8


COPY requirements.txt .
COPY app.py .
COPY dummy.json .
RUN chmod 775 dummy.json 

RUN redisurl="http://download.redis.io/redis-stable.tar.gz"
RUN curl -s -o redis-stable.tar.gz "http://download.redis.io/redis-stable.tar.gz"
RUN su root
RUN mkdir -p /usr/local/lib/
RUN chmod a+w /usr/local/lib/
RUN tar -C /usr/local/lib/ -xzf redis-stable.tar.gz
RUN rm redis-stable.tar.gz
RUN cd /usr/local/lib/redis-stable/ && make && make install
RUN redis-cli --version
RUN su root
RUN mkdir -p /etc/redis/
COPY 6379.conf /etc/redis/6379.conf
RUN redis-server /etc/redis/6379.conf

RUN pip install -r requirements.txt

EXPOSE 8081
CMD ["python3", "app.py", "--host", "0.0.0.0", "-p", "8081"]
