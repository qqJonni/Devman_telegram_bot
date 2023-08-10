FROM python:3
WORKDIR /devman

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python", "check_bot.py" ]


