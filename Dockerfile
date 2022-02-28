FROM python

WORKDIR /temp

COPY . .

RUN pip install -r rqs.txt

CMD ["python", "main.py"]