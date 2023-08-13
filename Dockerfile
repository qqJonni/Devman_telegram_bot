FROM python:3
WORKDIR /devman
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python", "check_bot.py" ]




