
class Stock:
    def __init__(self, symbol, company_name):
        
        self.__symbol = symbol
        self.__company_name = company_name

    
    def get_symbol(self):
        return self.__symbol


    def get_company_name(self):
        return self.__company_name

def display_stock_report(stocks):

    print(f"{'Company':<20} {'Symbol':<10}")
    print("-" * 30)
    

    for stock in stocks:
        print(f"{stock.get_company_name():<20} {stock.get_symbol():<10}")