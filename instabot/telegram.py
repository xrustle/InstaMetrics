import instabot.config as config
from instabot.insta import Insta
from instabot.msg import get, emoji
from instabot.db import db
import telebot
import schedule
import time
from threading import Thread
from pprint import pprint

telebot.apihelper.proxy = config.PROXY
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid != my_id:
        return 0
    bot.send_message(cid, get('ru', 'start'))


@bot.message_handler(commands=['unfollowers'])
def command_unfollowers(m):
    cid = m.chat.id
    if cid != my_id:
        return 0
    bot.send_message(cid, instagram.get_unfollowers(config.USER))


@bot.message_handler(commands=['emoji'])
def command_emoji(m):
    cid = m.chat.id
    if cid != my_id:
        return 0
    bot.send_message(cid, emoji('superstar'))


@bot.message_handler(content_types=["text"])
def print_message(m: telebot.types.Message):
    db.insert(m.json)


def send_mes():
    bot.send_message(my_id, "5 sec left")
    print('sended...')


class SendMessageEvery5Sec(Thread):
    def __init__(self):
        Thread.__init__(self)
        schedule.every(5).seconds.do(send_mes)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    # instagram = Insta()
    # SendMessageEvery5Sec().start()
    my_id = config.ID
    bot.polling()
