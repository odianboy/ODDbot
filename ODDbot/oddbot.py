import telebot

bot = telebot.TeleBot('1300891391:AAHQZZMenUmVngmU-TzeT7m9gWgvV9SpQwE')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row("hi", "bye")


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать... /start", reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == "hi":
        bot.send_message(message.chat.id, "Приветсвую...")
    elif message.text.lower() == "bye":
        bot.send_message(message.chat.id, "Прощай...")
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, "Думаю о вечном...")
        if message.text.lower() == "хорошо":
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIBMF9p8mDq3PMCCgvungLSAQYMbtitAAKfEwACKlUYAhpI0dTKqiFJGwQ")
    elif message.text.lower() == "ты робот?":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIBOF9p9FQqVm0osau8Qs9NDdF_0G2PAAKnEwACKlUYAm7Zx1iU2lYOGwQ")
    else:
        bot.send_message(message.chat.id, "Поробуй снова")


@bot.message_handler(content_types=["sticker"])
def sticker_id(message):
    print(message)


bot.polling()
