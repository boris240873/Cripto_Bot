
import telebot

TOKEN = '6553333129:AAEeC1vy_jquV4XsDpjVUU3YkB01HDgeHmM'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message: telebot.types.Message):

    bot.send_message(message.chat.id, 'hello')
bot.polling()









# import telebot
# from config import keys, TOKEN
# from utils import ConvertionException, CryptoConverter
#
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['start', 'help'])
# def help(message: telebot.types.Message):
#     text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
# <в какую валюту перевести> \
# <количество переводимой валюты>\nУвидить список всех доступных валют: /values'
#     bot.reply_to(message, text)
#
#
# @bot.message_handler(commands=['values'])
# def values(message: telebot.types.Message):
#     text = 'Доступные валюты:'
#     for key in keys.keys():
#         text = '\n'.join((text, key, ))
#     bot.reply_to(message, text)
#
# @bot.message_handler(content_types=['text', ])
# def convert(message: telebot.types.Message):
#     try:
#         values = message.text.split(' ')
#
#         if len(values) != 3:
#             raise ConvertionException('Слишком много  параметров')
#
#         quote, base, amount = values
#         total_base = CryptoConverter.convert(base, quote, amount)
#
#     except ConvertionException as e:
#         bot.reply_to(message, f'Ошибка пользователя.\n{e}')
#     except Exception as e:
#         bot.reply_to(message, f'Не удалось обработать команду\n{e}')
#
#     else:
#         text = f'Цена {amount} {quote} в {base} - {total_base}'
#         bot.send_message(message.chat.id, text)
#
# bot.polling()


# utils

# import requests
# import json
# from config import keys
#
#
# class ConvertionException(Exception):
#     pass
#
# class CryptoConverter:
#     @staticmethod
#     def convert(quote: str, base: str, amount: str):
#
#         if quote == base:
#             raise ConvertionException(f'Не удалось перевести одинаковые валюты: {base}.')
#
#         try:
#             quote_ticker = keys[quote]
#         except KeyError:
#             raise ConvertionException(f'Не удалось обработать валюту {quote}')
#
#         try:
#             base_ticker = keys[base]
#         except KeyError:
#             raise ConvertionException(f'Не удалось обработать валюту {base}')
#
#         try:
#             amount = float(amount)
#         except ValueError:
#             raise ConvertionException(f'Не удалось обработать количество {amount}')
#
#
#         r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
#         total_base = json.loads(r.content)[keys[base]]
#
#
#         return total_base


# config

# TOKEN = '6553333129:AAEeC1vy_jquV4XsDpjVUU3YkB01HDgeHmM'
#
# keys = {
#     'биткоин': 'BTC',
#     'эфириум': 'ETH',
#     'доллар': 'USD',
#     'рубль': 'RUB',
#     'евро': 'EUR'
# }













# import json
# import requests
# import telebot
# import telebot
# from config import keys,TOKEN
# from utils import ConvertionException, Cryptoconverter
#
#
# @bot.message_handler(commands=['start', 'help'])
# def help(message: telebot.types.Message):
#     text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
# <в какую валюту перевести> \
# <количество переводимой валюты>\nУвидить список всех доступных валют: /values'
#     bot.reply_to(message, text)
#
#
# @bot.message_handler(commands=['values'])
# def values(message: telebot.types.Message):
#     text = 'Доступные валюты:'
#     for key in keys.keys():
#         text = '\n'.join((text, key))
#     bot.reply_to(message, text)
#
# @bot.message_handler(content_types=['text'])
# def convert_result(message: telebot.types.Message):
#     try:
#         values = message.text.split(' ')
#
#         if len(values) != 3:
#             raise ConvertionException('Слишком много или слишком мало параметров')
#
#         base, quote, amount = values
#         total_base = Cryptoconverter.convert(base, quote, amount)
#         text = f'Цена {amount} {quote} в {base} - {total_base}'
#         bot.send_message(message.chat.id, text)
#
#
# bot.polling()

# TOKEN = '6553333129:AAEeC1vy_jquV4XsDpjVUU3YkB01HDgeHmM'

# bot = telebot.TeleBot(TOKEN)

# keys = {
#     'биткоин': 'BTC',
#     'эфириум': 'ETH',
#     'доллар': 'USD',
# }
#
# class ConvertionException(Exception):
#     pass
#
# @bot.message_handler(commands=['start', 'help'])
# def help(message: telebot.types.Message):
#     text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
# <в какую валюту перевести> \
# <количество переводимой валюты>\nУвидить список всех доступных валют: /values'
#     bot.reply_to(message, text)
#
#
# @bot.message_handler(commands=['values'])
# def values(message: telebot.types.Message):
#     text = 'Доступные валюты:'
#     for key in keys.keys():
#         text = '\n'.join((text, key))
#     bot.reply_to(message, text)
#
# @bot.message_handler(content_types=['text', ])
# def convert(message: telebot.types.Message):
#
#     values = message.text.split(' ')
#
#     if len(values) > 3:
#         raise ConvertionException('Слишком много параметров.')
#     if quote == base:
#         raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
#
#     quote_ticker, base_ticker = keys[quote], keys[base]
#     r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
#     total_base = json.loads(r.content)[keys[base]]
#     text = f'Цена {amout} {quote} в {base} - {total_base}'
#     bot.send_message(message.chat.id, text)
#
#
# bot.polling()
# #
#
#
#
# import telebot
# from config_1 import keys, TOKEN
# from utils import convertionException, Cryptoconverter
# TOKEN = '6320218482:AAFtQCgI6Uxlsoa8PjXwzLBpOcNjOn_Tv7s'
# keys = {
#     'евро': 'EUR',
#     'доллар': 'USD',
#     'рубль': 'RUB'
# }
# # import telebot
# # from config import TOKEN
# # from extensions import APIException, CryptoConverter
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(commands=['start', 'help'])
# def help(message: telebot.types.Message):
#     text = 'Чтобы начать работу введите команду боту в следующнм формате:\n<имя валюты цену которой он хочет узнать> \
# <имя валюты в которой надо узнать цену первой валюты> \
# <количество первой валюты>\nУвидеть список всех доступных валют: /values'
#     bot.reply_to(message, text)
#
#
# @bot.message_handler(commands=['values'])
# def values(message: telebot.types.Message):
#     text = 'Доступные валюты:'
#     for key in keys.keys():
#         text = '\n'.join((text, key,))
#     bot.reply_to(message, text)
#
#
# @bot.message_handler(content_types=['text', ])
# def convert(message: telebot.types.Message):
#     try:
#         values = message.text.split(' ')
#
#         if len(values) != 3:
#             raise APIException("Слишком много параметров.")
#
#             raise APIException("Мало параметров.")
#
#         base, quote, amount = values
#         total_base = CryptoConverter.get_price(base, quote, amount)
#     except APIException as e:
#         bot.reply_to(message, f'Ошибка пользователя\n{e}')
#     except Exception as e:
#         bot.reply_to(message, f'Не удалось обработать команду\n{e}')
#     else:
#         text = f'Цена {amount} {base} в {quote} - {total_base}'
#         bot.send_message(message.chat.id, text)
#
#
# bot.polling(none_stop=True)
#
# import requests
# import json
#
# from config_1 import keys
#
#
# class APIException(Exception):
#     pass
#
#
# class CryptoConverter:
#     @staticmethod
#     def get_price(base: str, quote: str, amount: float):
#
#         if quote == base:
#             raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
#
#         try:
#             quote_ticker = keys[quote]
#         except KeyError:
#             raise APIException(f'Не удалось обработать валюту {quote}')
#
#         try:
#             base_ticker = keys[base]
#         except KeyError:
#             raise APIException(f'Не удалось обработать валюту {base}')
#
#         try:
#             amount = float(amount)
#         except ValueError:
#             raise APIException(f'Не удалось обработать количество валюты{amount}')
#
#         if amount <= 0:
#             raise APIException(f'Невозможно конверстировать количество валюты меньше или равное 0')
#
#         r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
#         total_base = json.loads(r.content)[keys[quote]] * amount
#
#         return total_base