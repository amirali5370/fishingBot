import telebot
from database.base import SessionLocal
from database.user import User
from keyboards import *
from messages import *
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    if len(message.text) > 7:
        code = message.text.split(" ")[1]
        bot.reply_to(message,code)
    bot.send_message(message.chat.id,start_mess(message.from_user,message.chat.id),reply_markup=main_key())


@bot.callback_query_handler(func= lambda x:True)
def callback_handler(call):
    return call.data


@bot.message_handler(func= lambda x:True)
def other(message):
    return message.text


bot.polling()



# db = SessionLocal()
# new_user = User(username=username, age=age)
# db.add(new_user)
# db.commit()
# db.close()