import telebot
from telebot import types
import random
import openpyxl


bot = telebot.TeleBot('853176372:AAFG6yK7G3zOrrYt76vxrOQrmeZ4bsO5sSY')




@bot.message_handler(commands=['start'])
def start_message(message):
    str = message.from_user.username
    try:
        vitanya(message)
    finally:
        flag = True

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.reply_to(message, 'Хто я?')

@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.reply_to(message, 'Я тебе не розумію')

def vitanya(message):
    name = message.from_user.username
    wb = openpyxl.reader.excel.load_workbook(filename = "sample.xlsx")
    wb.active = 0
    sheet = wb.active
    i = 1
    while(str(sheet['A'+ str(i)].value) != 'None'):
        i=i+1
    number = i-2 #кількість учасників
    test = name
    c = 2 #counter
    while ((str(sheet['B'+ str(c)].value) != test) and c<15):
        c=c+1
    if(c==15):
        bot.reply_to(message, 'Ви не реєструвалися на обмін')
    else:
        bot.reply_to(message, "Привіт " + str(sheet['G'+ str(c)].value) + ". Ти маеш надіслати свою книгу  "  + str(sheet['E'+ str(c)].value))



bot.polling()
