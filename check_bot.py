import logging
import os
import textwrap
import requests
import time
import telegram
from dotenv import load_dotenv

logger = logging.getLogger('logger')
URL = 'https://dvmn.org/api/long_polling/'


class TelegramBotHandler(logging.Handler):

    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.tg_bot = tg_bot
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def check_lesson(timestamp, tokens):
    headers = {'Authorization': f'Token {tokens}'}
    payloads = {'timestamp': timestamp}
    response = requests.get(URL, headers=headers, params=payloads, timeout=120)
    response.raise_for_status()
    return response.json()


def send_message(bot, result, chat_id):
    checking_result = result['new_attempts'][0]
    title = checking_result['lesson_title']
    url = checking_result['lesson_url']

    if checking_result['is_negative']:
        text_message = f'''
                    У вас проверили работу "{title}"
                    К сожалению, в работе нашлись ошибки.
                    https://dvmn.org{url}'''
    else:
        text_message = f'''
                    У вас проверили работу "{title}" 
                    Преподавателю всё понравилось, можно приступать к следующему уроку! 
                    https://dvmn.org{url}'''
    bot.send_message(chat_id=chat_id, text=textwrap.dedent(text_message))


def main():
    load_dotenv()
    devman_token = os.getenv('DVMN_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')

    bot = telegram.Bot(token=telegram_token)

    logger.setLevel(logging.INFO)
    handler = TelegramBotHandler(bot, telegram_chat_id)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info('Бот запущен и приветствует вас!')

    timestamp = None

    while True:
        try:
            check_lesson = check_lesson(timestamp, devman_token)
            if check_lesson['status'] == 'timeout':
                timestamp = check_lesson['timestamp_to_request']
            else:
                timestamp = check_lesson['last_attempt_timestamp']
                send_message(bot, check_lesson, telegram_chat_id)
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            logger.exception('Бот поймал ошибку: ')
            time.sleep(60)
            continue
        except Exception:
            logger.exception('Бот поймал ошибку: ')


if __name__ == '__main__':
    main()
