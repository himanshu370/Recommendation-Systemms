FROM ubuntu:20.04

RUN apt update && apt install -y htop python3
RUN apt install -y python3-pip

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--reload"]