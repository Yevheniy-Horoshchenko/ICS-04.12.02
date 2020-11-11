""" модуль для отримання даних про постачання та вивід їх на екран
"""


def get_prices():
    """ повертає вміст файла 'prices.txt` у вигляді списка
    """
    with open('./data/prices.txt') as prices_file:
        from_file = prices_file.readlines()

    # накопичувач цін
    prices_list = []

    for line in from_file:
        line_list = line.split(';')
        prices_list.append((line_list))

    return prices_list

def get_products():
    """повертає вміст файла 'products.txt' у вигляді списка
    """
 
    with open ('./data/products.txt') as products_file:
        from_file = products_file.readlines()

    products_list = []

    for line in from_file:
        line_list = line.split()
        products_list.append(line_list)
def show_prices(prices):
    

    # задати інтервал виводу
    price_code_from = input("З якого кода ціна? ")
    price_code_to   = input("По який код ціна? ")
    
    # накопичує кількість виведених рядків
    kol_lines = 0

    for price in prices:
        if  price_code_from  <= price[0] <= price_code_to:
            print("код: {:3} середня ціна за 2007 рік: {:7} 2011 рік: {:7} 2017 рік: {:6}назва ринку: {:10}".format(price[0], price[1], price[3], price[4],price[5]))
            kol_lines += 1

    # перевірити чи був вивід хоча б одного рядка
    if kol_lines == 0:
        print("По вашому запиту цін не знайдено!")
    

prices = get_prices()
show_prices(prices)