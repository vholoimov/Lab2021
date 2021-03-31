import telebot
from telebot import types
import random

bot = telebot.TeleBot('839516197:AAH0X-XkGsnUKzs5rjceHqbxdy7idmWZEu0')




@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Welcome to the club buddy')

@bot.message_handler(commands=['rules'])
def start_message(message):
    bot.reply_to(message, 'Щоб бути впевненим, що ти робиш усе правильно, користуйся наступними правилами: \n Поважай чужу власність і поводься з книжечкою обережно \n Пам’ятай що це буккросінг, тому книжечка не повинна лежати у тебе на полиці рік, у тебе буде місяць до того як потрібно буде відправити книгу новій людині \n Щоб дізнатися, як краще передати книгу, краще написати особисте повідомлення \n Якщо тобі ніхто не написав, можеш тикнути /mybook і подивитись, хто має відпавити книгу тобі \n ті сонечно')


@bot.message_handler(commands=['mybook'])
def start_message(message):
    name = message.from_user.username
    wb = openpyxl.reader.excel.load_workbook(filename = "sample.xlsx")
    wb.active = 0
    sheet = wb.active
    i = 1
    while(str(sheet['B'+ str(i)].value) != 'None'):
        i=i+1
    number = i #кількість учасників
    test = name
    c = 2 #counter
    while ((str(sheet['F'+ str(c)].value) != test) and c<number):
        c=c+1
    if(c==number):
        bot.send_message(message.chat.id, 'Ви не реєструвалися на обмін')
    else:
        bot.send_message(message.chat.id, "Тобі мала надіслати книжку осьо ця людина:  " str(sheet['С'+ str(c)].value))



@bot.message_handler(content_types=['text'])
def send_text(message):
    st0 = message.text.lower()
    if st0 == 'гачи':
        gachi(message)
    if st0 == 'время gachimuchi':
        gachimuchi(message)
    ch0 = chch(message)
    if ch0 == 1:
        st1 = str(message.message_id)
        bot.reply_to(message, st1)

@bot.message_handler(content_types=['photo', 'video','document', 'audio'])
def send_text(message):
    ch0 = chch(message)
    if ch0 == 1:
        st1 = str(message.message_id)
        bot.reply_to(message, st1)

def gachi(message):
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_audio = types.InlineKeyboardButton(text='Аудио', callback_data='audio'); #кнопка «Да»
    keyboard.add(key_audio); #добавляем кнопку в клавиатуру
    key_gif= types.InlineKeyboardButton(text='Gif', callback_data='gif');
    keyboard.add(key_gif);
    key_picture= types.InlineKeyboardButton(text='Картинка', callback_data='picture');
    keyboard.add(key_picture);
    question = 'В каком формате вы хотите получить GACHI';
    bot.send_message(message.chat.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    id0 = call.message.chat.id
    if call.data == "audio": #call.data это callback_data, которую мы указали при объявлении кнопки
         #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Сейчас кину тебе аудио GACHI')
        aud(id0)
    elif call.data == "gif":
        bot.send_message(call.message.chat.id, 'Сейчас кину тебе gif GACHI')
        gif(id0)
    elif call.data == "picture":
        bot.send_message(call.message.chat.id, 'Сейчас кину тебе картинку GACHI')
        pict(id0)

def gachimuchi(message):
    bot.set_chat_title(message.chat.id, 'GACHICHAT')
    photo = open('C:/Users/Валерий/Desktop/gachibot/gachi.jpg', 'rb')
    bot.set_chat_photo(message.chat.id, photo)

def chch(message):
    if message.chat.id == -322542240:
        return 1
    else:
        return 0

def pict(id0):
    k = random.randint(1,4)
    if k == 1:
        bot.forward_message(id0, -322542240, 87)
    if k == 2:
        bot.forward_message(id0, -322542240, 81)
    if k == 3:
        bot.forward_message(id0, -322542240, 83)
    if k == 4:
        bot.forward_message(id0, -322542240, 85)

def aud(id0):
    k = random.randint(1,10)
    if k == 1:
        bot.forward_message(id0, -322542240, 213)
    if k == 2:
        bot.forward_message(id0, -322542240, 215)
    if k == 3:
        bot.forward_message(id0, -322542240, 217)
    if k == 4:
        bot.forward_message(id0, -322542240, 219)
    if k == 5:
        bot.forward_message(id0, -322542240, 220)
    if k == 6:
        bot.forward_message(id0, -322542240, 222)
    if k == 7:
        bot.forward_message(id0, -322542240, 225)
    if k == 8:
        bot.forward_message(id0, -322542240, 226)
    if k == 9:
        bot.forward_message(id0, -322542240, 231)
    if k == 10:
        bot.forward_message(id0, -322542240, 231)

def gif(id0):
    k = random.randint(1,23)
    if k == 1:
        bot.forward_message(id0, -322542240, 125)
    if k == 2:
        bot.forward_message(id0, -322542240, 127)
    if k == 3:
        bot.forward_message(id0, -322542240, 129)
    if k == 4:
        bot.forward_message(id0, -322542240, 131)
    if k == 5:
        bot.forward_message(id0, -322542240, 133)
    if k == 6:
        bot.forward_message(id0, -322542240, 135)
    if k == 7:
        bot.forward_message(id0, -322542240, 137)
    if k == 8:
        bot.forward_message(id0, -322542240, 139)
    if k == 9:
        bot.forward_message(id0, -322542240, 141)
    if k == 10:
        bot.forward_message(id0, -322542240, 143)
    if k == 11:
        bot.forward_message(id0, -322542240, 145)
    if k == 12:
        bot.forward_message(id0, -322542240, 147)
    if k == 13:
        bot.forward_message(id0, -322542240, 149)
    if k == 14:
        bot.forward_message(id0, -322542240, 182)
    if k == 15:
        bot.forward_message(id0, -322542240, 184)
    if k == 16:
        bot.forward_message(id0, -322542240, 186)
    if k == 17:
        bot.forward_message(id0, -322542240, 188)
    if k == 18:
        bot.forward_message(id0, -322542240, 190)
    if k == 19:
        bot.forward_message(id0, -322542240, 192)
    if k == 20:
        bot.forward_message(id0, -322542240, 194)
    if k == 21:
        bot.forward_message(id0, -322542240, 196)
    if k == 22:
        bot.forward_message(id0, -322542240, 198)
    if k == 23:
        bot.forward_message(id0, -322542240, 200)


bot.polling()

  bot.send_message(message.chat.id, "Привіт " + str(sheet['B'+ str(c)].value) + ".\nТи маеш надіслати свою книгу  "  + str(sheet['E' + str(c)].value) + "  @"+ str(sheet['F' + str(c)].value)+".\nЯк$
