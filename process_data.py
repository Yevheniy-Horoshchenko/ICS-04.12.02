"""формування аналізу цін по рокам
"""

# підключити функції з модуля `data_service`
from data_service import get_products, get_prices

# структура накопичувача записів вихідних даних
analiz = {

    'nazva_rinku'     : '',    # назва ринку   
    'nazva_tovaru'    : '',    # назва товару
    'system_units'    : '',    # системні одиниці
    '2007_price'      : 0.0,   # ціна за 2007 рік
    '2008_price'      : 0.0,   # ціна за 2008 рік
    'vidsotok_do_2007': 0.0,   # відсоток до 2007
    '2011_price'      : 0.0,   # ціна за 2011 рік
    'vidsotok_do_2008': 0.0,   # відсоток до 2008
    '2017_price'      : 0.0,   # ціна за 2017 рік
    'vidsotok_do_2011': 0.0    # відсоток до 2011


}


prices = get_prices()
products = get_products()

def create_analiz():
    """формування аналізів змін цін на продовольчі товари
    """
    def get_product_name(product_code):
        """повертає назву продукту по його коду

        Args:
            product_code ([type]): код продукту

        Returns:
            [type]: назва продукта
        """

        for product in products:
            if product[0] == product_code:
                return product[1]
        
        return "*** код продукту не знайдений"
    # накопичувач аналізів 
    analiz_list = []

    for price in prices:
        
        # створити копію шаблона
        analiz_lvl = analiz.copy()

        analiz_lvl['nazva_rinku']      = price[5] 
        analiz_lvl['nazva_tovaru']     = get_product_name(price[1])
        analiz_lvl['system_units']     = get_product_name(price[2]) 
        analiz_lvl['2007_price']       = price[1]
        analiz_lvl['2008_price']       = price[2]
        analiz_lvl['vidsotok_do_2007'] = float(analiz_lvl['2008_price']) / float(analiz_lvl['2007_price']) * 100
        analiz_lvl['2011_price']       = price[3]
        analiz_lvl['vidsotok_do_2008'] = float(analiz_lvl['2011_price']) / float(analiz_lvl['2008_price']) * 100
        analiz_lvl['2017_price']       = price[4]
        analiz_lvl['vidsotok_do_2011'] = float(analiz_lvl['2017_price']) / float(analiz_lvl['2011_price']) * 100
        
        
        analiz_list.append(analiz_lvl)

    return analiz_list

result = create_analiz()



