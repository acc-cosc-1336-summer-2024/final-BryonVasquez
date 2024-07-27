from question_b import create_multiplication_table, display_multiplication_table
def main():
    while True:
        
        try:
            rows = int(input("Enter the number of rows for the multiplication table: "))
            cols = int(input("Enter the number of columns for the multiplication table: ")) 
        except ValueError:
            print("Invalid input. Please enter integer values.")      
        
        table = create_multiplication_table(rows, cols)
        display_multiplication_table(table)
        

       
        user_choice = input("Do you want to create another table? (yes/no): ").strip().lower()
        if user_choice != 'yes':
            print("Exiting the program.")
            break

main()