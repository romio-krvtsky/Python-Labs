FROM python

WORKDIR /lab1

COPY . .

RUN pip install -r rqs.txt

CMD ["python", "main.py"]