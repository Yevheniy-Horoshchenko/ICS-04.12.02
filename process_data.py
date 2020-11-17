"""аналіз зміни рівня цін на продовольчі товари
"""

from data_service import get_prices, get_products

analiz = {

    'rinok_name'   : '',   #найменування ринку
    'tovar_name'   : '',   #найменування товара
    'system_units' : '',   #системні одиниці
    '2007_price'   : 0.0,  #ціна за 2007 рік
    '2008_price'   : 0.0,  #ціна за 2008 рік
    'vidsotok_2007': 0.0,  #у % до 2007
    '2011_price'   : 0.0,  #ціна за 2011 рік
    'vidsotok_2008': 0.0,  #у % до 2008
    '2017_price'   : 0.0,  #ціна за 2017 рік
    'vidsotok_2011': 0.0   #у % до 2011


}

print(get_prices())
print(get_products())
