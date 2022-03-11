FROM python:3.8

COPY requirements.txt .
COPY app.py .
COPY templates templates
COPY templates/base.html templates/base.html
COPY templates/index.html templates/index.html

RUN pip install -r requirements.txt

EXPOSE 8085

CMD ["python3", "app.py", "--host", "0.0.0.0", "-p", "8085"]



