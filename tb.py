import sys
import telebot
from final import words


token = '555517666:AAEk1XHnuS89vqRS_zhfiuEVPwUi9X7il-A'
bot = telebot.TeleBot(token)
used = []
first_letter = []
source = []
words.get_words('word_rus.txt', source, first_letter)


@bot.message_handler(content_types=['text'])
def word_game(message):
            if message.text in used:
                bot.send_message(message.chat.id, text='Это слово уже было. Давай еще раз.')
                sys.exit(0)
            elif message.text[0].lower() not in first_letter:
                bot.send_message(message.chat.id, text="У меня больше нет слов на эту букву")
                sys.exit(0)
            for i in source:
                if message.text[-1] == i[0]:
                    bot.send_message(message.chat.id, text=i)
                    source.remove(i)
                    first_letter.remove(i[0])
                    used.append(message.text)
                    used.append(i)
                    break

            if message == 'exit()':
                sys.exit(0)


if __name__ == '__main__':
    bot.polling(none_stop=True)
