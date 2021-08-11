import re
import operator
from collections import defaultdict

# Используя регулярные врыражения, создадим шаблон, подходящий для всех полей с инфрмацией
REGEXP = re.compile('([a-z_]+):("[\w -]+"|\d+)')


# Функция для перевода информации в словари
def parse_to_obj(doc):
    result = {}
    for i in doc:
        result[i[0]] = i[1]
    return result

    # С помощью шаблона регулярного выражения представим информацию из полей в виде списка словарей


def main():
    list_of_dicts = []
    with open('C:/Users/yatov/Downloads/Telegram Desktop/input.txt', 'r') as file:
        for row in file:
            list_of_dicts.append(parse_to_obj(REGEXP.findall(row)))

    # Занесем в новые словари информацию о количестве сообщений типа Validation error, AntiFraud, Unkown user.
    # А также соберем в список значения полей user_id и message.

    dict_for_count = {}
    dict_for_user_type = {}
    message_plus_user_id = []

    for i in list_of_dicts:
        if i['function'] == '"MakePayment"' and i['message'] in ['"Validation error"', '"Unkown user"', '"AntiFraud"']:
            user_id = i['user_id']
            message = i['message']
            dict_for_count[message] = dict_for_count.get(message, 0) + 1

            user_type = i['user_type']
            dict_for_user_type[message] = dict_for_user_type.get(message, {})
            dict_for_user_type[message][user_type] = dict_for_user_type[message].get(user_type, 0) + 1

            message_plus_user_id.append((user_id, message))

    # Сортируем сообщения об ошибках по количеству в порядке возрастания и наиболее частое значение поля user_type для
    # каждого типа сообщений.

    sorted_dict_for_count = {}
    sorted_keys = sorted(dict_for_count, key=dict_for_count.get, reverse=True)

    for i in sorted_keys:
        sorted_dict_for_count[i] = dict_for_count[i]

    f = open("output.txt", "w")

    for message, count in sorted_dict_for_count.items():
        max_type = max(dict_for_user_type[message].items(), key=operator.itemgetter(1))
        f.write(f'message {message}, count {count}, most count user type {max_type[0]}\n')

    f.write(f'\n')

    for i in message_plus_user_id:
        f.write(f'{i[0]}\t{i[1]}\n')


if __name__ == '__main__':
    main()
