FROM python:3.8.10-alpine
#RUN pip install requests 
COPY App.py /

CMD [ "python3","App.py" ]