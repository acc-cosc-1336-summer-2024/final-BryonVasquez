#add import 

def main():
    # Initialize an empty list to store numbers
    numbers = []

    # Get 5 numbers from the user
    for i in range(5):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)

    # Calculate the required data
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    # Display the results
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average}")

if __name__ == "__main__":
    main()