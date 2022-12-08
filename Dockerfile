FROM python

ADD cal.py .

CMD [ "python", "./cal.py"]