
import telebot

TOKEN = '6553333129:AAEeC1vy_jquV4XsDpjVUU3YkB01HDgeHmM'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message: telebot.types.Message):

    bot.send_message(message.chat.id, 'hello')
bot.polling()









