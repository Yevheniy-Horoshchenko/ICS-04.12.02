""" головний модуль задачі
- виводить розрахункову таблицю на екран та в файл
- виводить первинні данні на екран
"""

import os
from process_data import create_analiz


MAIN_MENU = \
"""
~~~~~~~  Аналіз зміни рівня цін на продовольчі товари ~~~~~~~

1 - вивід заявок на екран
2 - запис аналізу в файл
3 - вивід списка продуктів
4 - вивід списка цін
0 - завершення роботи
----------------------------
"""

TITLE = "АНАЛІЗ ЗМІНИ РІВНЯ ЦІН НА ПРОДОВОЛЬЧІ ТОВАРИ"

HEADER = \
"""
=======================================================================================================================================
  Назва ринку |   Назва товара   | Одиниця виміру | 2007 |         2008            |           2011          |            2017        |
=======================================================================================================================================
                                                         |грн |    у % до 2007     |грн |   у % до 2008      |грн |     у % до 2011   |
=======================================================================================================================================

"""

FOOTER = \
'''
=======================================================================================================================================

'''

STOP_MESSAGE = 'Для продовження натисніть <Enter>'

def show_analiz(analiz_list):
    """виводиить таблицю аналізу 

    Args:
        analiz_list ([type]): список аналізу
    """
    print(f"\n\n{TITLE:^91}")
    print(HEADER)

    for analiz in analiz_list:
        print(f"{analiz['nazva_rinku']:15}",
              f"{analiz['nazva_tovaru']:13}",
              f"{analiz['system_units']:^14}",
              f"{analiz['2007_price']:5}",
              f"{analiz['2008_price']:7}",
              f"{analiz['vidsotok_do_2007']:^17f}",
              f"{analiz['2011_price']:10}",
              f"{analiz['vidsotok_do_2008']:13}",
              f"{analiz['2017_price']:^9}",
              f"{analiz['vidsotok_do_2011']:1}"

              )

    print(FOOTER)


def write_analiz(analiz_list):
    """записує список заявок у текстовий файл

    Args:
        zajavka_list ([type]): список заявок
    """

    with open('.\data\analiz.txt', 'w') as analiz_file:
        for analiz in analiz_list:
            line = \
               analiz['nazva_rinku'] + ';' +             \
               analiz['nazva_tovaru'] + ';' +            \
               analiz['system_units'] + ';' +            \
               str(analiz['2007_price']) + ';' +         \
               str(analiz['2008_price']) + ';' +         \
               str(analiz['vidsotok_do_2007'])  +        \
               str(analiz['2011_price']) + ';' +         \
               str(analiz['vidsotok_do_2008']) + ';' +   \
               str(analiz['2017_price']) + ';' +         \
               str(analiz['vidsotok_do_2011']) + '\n' 
               
            analiz_file.write(line)  
            
    print('Файл успішно записано ...')





while True:
    
    # вивід головного меню
    os.system('clear')   
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")
    
    # обробка команд користувача
    if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)
        
    elif command_number == '1':
        analiz_list = create_analiz()
        show_analiz(analiz_list)
        input(STOP_MESSAGE)