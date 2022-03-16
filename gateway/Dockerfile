FROM python:3.8

WORKDIR /gateway
COPY requirements.txt .
COPY app.py .
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh
RUN chmod +x app.py
 
#ENV FLASK_APP=app.py FLASK_RUN_HOST=0.0.0.0
COPY templates templates
COPY templates/base.html templates/base.html
COPY templates/index.html templates/index.html



RUN pip install -r requirements.txt

#EXPOSE 8085
EXPOSE 8085 
#ENTRYPOINT ["./docker-entrypoint.sh" ]
ENTRYPOINT ["python"]
CMD ["app.py", "--host", "0.0.0.0"]



