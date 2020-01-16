import instabot.config as config
from  instabot.insta import insta
import telebot
import instabot.emoji as emoji
from telebot import apihelper

apihelper.proxy = config.PROXY
bot = telebot.TeleBot(config.TOKEN)
my_id = config.ID
instagram = insta()


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid != my_id:
        return 0
    bot.send_message(cid, 'Hello, stranger!')


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
    bot.send_message(cid, emoji.SUPERSTAR)


bot.polling()
