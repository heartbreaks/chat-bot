FROM python:3.12

WORKDIR /app

RUN pip install --upgrade pip wheel setuptools
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python source/start_tg_bot.py