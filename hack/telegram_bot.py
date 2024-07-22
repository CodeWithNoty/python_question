import telebot

Token = "6436436918:AAEGbD4k35RCU3mZjBzMcAsF4bqCoqnpbQk"

bot = telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start (message):
    bot.reply_to(message,"welcome to dethcode")

@bot.message_handler(['help'])
def help (message):
    bot.reply_to(message,"""/start 
                 -> greating /help 
                 -> will you give all commands list 
   if you see mia khalif photo that you feel
     """)


@bot.message_handler()
def custom(message):
 try:
    msg = eval(message.text.strip())
 except Exception as e:
    msg ="this can not be evaluted "
    bot.reply_to(message,msg)    

bot.polling()