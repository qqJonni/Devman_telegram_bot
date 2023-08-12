FROM python:3
WORKDIR /devman
COPY requirements.txt requirements.txt

COPY . .
RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade setuptools
CMD [ "python", "check_bot.py" ]




