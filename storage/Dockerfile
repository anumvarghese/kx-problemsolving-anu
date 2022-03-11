FROM python:3.8


COPY requirements.txt .
COPY app.py .
COPY dummy.json .
RUN chmod 775 dummy.json 


RUN pip install -r requirements.txt

EXPOSE 8081
CMD ["python3", "app.py", "--host", "0.0.0.0", "-p", "8081"]
