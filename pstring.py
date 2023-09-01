# -------------------------------------------------------------------
# модуль pstring
# Функции для работы со строками
#
# (C) 2020 Ivan Genik, Perm, Russia
# Released under GNU Public License (GPL)
# email igenik@rambler.ru
# ------------------------------
import re

def print_string(the_list) -> None:
    print(len(the_list))
    for stri in the_list:
        print(stri, end=' ')
    print('+')

def num_words_in_string(s: str) -> int:
    return len(re.split('\s+', s))

def swlz(num:int, nposit:int) -> str: # строка с ведущими нулями
    """
    https://ru.stackoverflow.com/questions/628701/Вывод-числа-с-ведущими-нолями
    Вывод числа с ведущими нолями
    :param num:  число для преобразования в строку
    :param nposit: всего позиций в строке
    :return: строка с ведущими нулями
    """
    return str(num).zfill(nposit)



# print(re.sub(r'\D', '', 'Fjkoweuqe -1245 654lfr'))
# print(num_words_in_string('In the hole in the ground there lived a   hobbit')) # 10
# print(num_words_in_string('В  яме в  земле   жил   хоббит')) # 6
# print(num_words_in_string('min1')) # 1

# Проработать строки и регулярные выражения
# pythonist.ru/s/proverka-yavlyaetsya-li-stroka-palindromom/?utm_source=turbo_turbo
# https://habr.com/ru/post/349860/
