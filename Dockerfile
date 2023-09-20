FROM python

WORKDIR /thunder_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

COPY ./dependencies ./dependencies

CMD ["python", "./main.py"]


