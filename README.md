## Бот для отправки уведомлений о проверке работ.

Позволяет получать от бота в Telegram уведомления о проверке работ на сайте 
веб-разработчиков [Девман](https://dvmn.org).  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/0tR2gm8/image.jpg" alt="image" border="0"></a>

### Как установить

#### Скачать 

Python3 должен быть уже установлен.
[Скачать](https://github.com/Araime/devman-bot/archive/master.zip) этот репозиторий себе на компьютер.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.

#### Быстрая настройка venv

Начиная с Python версии 3.3 виртуальное окружение идёт в комплекте в виде модуля
venv. Чтобы его установить и активировать нужно выполнить следующие действия в
командной строке:  

Указать скачанный репозиторий в качестве каталога.
```sh
cd C:\Users\ваш_пользователь\Downloads\папка_репозитория
```
Установить виртуальное окружение в выбранном каталоге.
```sh
Python -m venv env
```
В репозитории появится папка виртуального окружения env  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Hn4C6PD/image.png" alt="image" border="0"></a>

Активировать виртуальное окружение.
```sh
env\scripts\activate
```
Если всё сделано правильно, вы увидите в командной строке (env) слева от пути 
каталога.  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/MZ72r22/2.png" alt="2" border="0"></a>

#### Установить зависимости

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки 
зависимостей:

```sh
pip install -r requirements.txt
```

#### Переменные окружения

Создайте в корне репозитория файл `.env` и добавьте в него следующие строки:

```sh
DVMN_TOKEN=персональный_токен
TELEGRAM_TOKEN=токен_telegram_бота
TELEGRAM_CHAT_ID=ваш_персональный_chat_id
```

Персональный токен можно получить, на сайте [Девман](https://dvmn.org/api/docs/).  
Создать бота для Telegram и узнать его токен можно у [Отца Ботов](https://telegram.me/BotFather).  
Свой chat_id можно получить у [userinfobot](https://telegram.me/userinfobot).

### Запуск

Найти вашего бота в Telegram и написать ему сообщение `/start`

Запуск скрипта выполняется командой:

```sh
python check_bot.py
```
