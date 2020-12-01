"""формування заявок на устаткування по магазину
"""

# підключити функції з модуля `data_service`
from data_service import get_products, get_prices

# структура накопичувача записів вихідних даних
analiz = {

    'nazva_rinku'     : '',    # назва устаткування   
    'nazva_tovaru'    : '',    # назва клієнта
    'system_units'    : '',    # номер заказу
    '2007_price'      : 0.0,     # кількість
    '2008_price'      : 0.0,   # ціна
    'vidsotok_do_2007': 0.0,
    '2011_price'      : 0.0,    # сума
    'vidsotok_do_2008': 0.0,
    '2017_price'      : 0.0,
    'vidsotok_do_2011': 0.0


}


prices = get_prices()
products = get_products()

def create_analiz():
    """формування заявок на устаткування
    """
    def get_product_name(product_code):
        """повертає назву клієнта по його коду

        Args:
            client_code ([type]): код клієнта

        Returns:
            [type]: назва клієнта
        """

        for product in products:
            if product[0] == product_code:
                return product[1]
        
        return "*** код клієнта не знайдений"
    # накопичувач заявок 
    analiz_list = []

    for price in prices:
        
        # створити копію шаблона
        analiz_tmp = analiz.copy()

        analiz_tmp['nazva_rinku']      = price[5]  
        analiz_tmp['2007_price']       = price[2]
        analiz_tmp['2008_price']       = price[4]
        analiz_tmp['vidsotok_do_2007'] = analiz_tmp['2008_price'] % analiz_tmp['2007_price']
        analiz_tmp['2011_price']       = price[5]
        analiz_tmp['vidsotok_do_2008'] = analiz_tmp['2011_price'] % analiz_tmp['2008_price']
        analiz_tmp['2017_price']       = price[6]
        analiz_tmp['vidsotok_do_2011'] = analiz_tmp['2017_price'] % analiz_tmp['2011_price']
        analiz_tmp['nazva_tovaru']     = get_product_name(price[0])
        analiz_tmp['system_units']     = get_product_name(price[1])
        
        analiz_list.append(analiz_tmp)

    return analiz_list

result = create_analiz()


