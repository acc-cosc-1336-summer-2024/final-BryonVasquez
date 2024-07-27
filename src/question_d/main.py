from question_d import Stock
 
def main():
    
    stocks = [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]

    
    print(f"{'Symbol':<10} {'Company Name'}")
    print("-" * 30)
    
    for stock in stocks:
        print(f"{stock.get_symbol():<10} {stock.get_company_name()}")

main()