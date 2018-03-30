import sys


def get_words(file, source, first_letter):
    with open(file) as f:
        for line in f:
            source.append(line.strip())
            first_letter.append(line[0])
        return source, first_letter


"""
def word_game():
        while 1:
            message = str(input()).lower()
            if message in used:
                print('Это слово уже было. Давай еще раз.')
                continue
            elif message[0] not in first_letter:
                print("У меня больше нет слов на эту букву")
                sys.exit(0)
            for i in source:
                if message[-1] == i[0]:
                    print(i)
                    source.remove(i)
                    first_letter.remove(i[0])
                    used.append(message)
                    used.append(i)
                    break


            if message == 'exit()':
                sys.exit(0)"""