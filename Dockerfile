FROM python:3.6.1
WORKDIR /traviscipython
ADD . /traviscipython
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","hello_world_app.py"]
