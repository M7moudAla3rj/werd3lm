import telebot
import schedule
import time

bot=telebot.TeleBot("1967626202:AAFykDZY-cKrU7UmOCkBxqTKAb97RxbTKCg")

i=0
chat_id="1202602736"
#chat_id2=""




imege="imeges/"+str(i)+".jpg"





@bot.message_handler(commands=['start'])
def start (message):
  bot.reply_to(message , "welcome")
  
@bot.message_handler(func=lambda message : True)
def mes (message):
  bot.reply_to(message , "شو بدك ؟")

def imeges ():

  bot.send_message(chat_id , "ورد اليوم من الدراسة")
  #bot.send_message(chat_id2 , "ورد اليوم من الدراسة")

  img=open (imege , 'rb')

  bot.send_photo(chat_id, img)
 # bot.send_photo(chat_id2, img)

def i ():

  i = i + 1

schedule.every(1).minutes.do(imeges)

#schedule.every().day.at("17:30:01").do(i)

while True:

  schedule.run_pending()
  bot.polling()

