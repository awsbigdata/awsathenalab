FROM python:2.7-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python dummy.py password
RUN python mockdataCreation.py
CMD ["python","app.py"]
