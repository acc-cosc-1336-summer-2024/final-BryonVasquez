
from question_c import stock_purchase_history


def main():
    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        
        option = input("Please select an option: ").strip()

        if option == '1':
            stock_purchase_history()
        elif option == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please select a valid option from the menu.")

main()