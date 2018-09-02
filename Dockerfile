FROM python:3.6
RUN apt update && apt install python-dev -y
COPY . /home
RUN cd /home && pip install -r requirements.txt
EXPOSE 5000
WORKDIR /home/app
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-", "--chdir", "/home/app"]
CMD ["app:app"]
