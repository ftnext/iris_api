FROM python:3.6
RUN apt update && apt install python-dev -y
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY app /app
WORKDIR /app
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-"]
CMD ["app:app"]
