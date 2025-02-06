FROM python:3.10

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
