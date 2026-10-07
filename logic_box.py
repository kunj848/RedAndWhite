"""
Project: Logic Box
Objective: Pattern Generator and Number Analyzer
This program emphasizes control structures, loops (for and while),
the range() function, control statements (break, continue, pass),
and nested loops.
"""

def generate_pattern():
    """Generates a right-angled triangle pattern based on user input."""
    while True:
        try:
            rows_input = input("Enter the number of rows for the pattern: ")
            rows = int(rows_input)
            
            if rows <= 0:
                print("Error: Number of rows must be a positive integer. Please try again.\n")
                continue
            
            print("\nPattern:")
            # Using nested loops to print the right-angled triangle
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print("*", end="")
                print()  # Move to the next line
            print()
            break  # Exit the loop once pattern is printed
            
        except ValueError:
            print("Invalid input! Please enter a valid whole number.\n")


def analyze_numbers():
    """Analyzes a range of numbers: identifies odd/even and calculates sum."""
    while True:
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            
            if end < start:
                print("Error: The end of the range must be greater than or equal to the start. Please try again.\n")
                continue
            
            total_sum = 0
            
            # Using range() and a for loop to iterate over the range inclusive of end
            for num in range(start, end + 1):
                total_sum += num
                
                # Check even or odd
                if num % 2 == 0:
                    print(f"Number {num} is Even")
                else:
                    print(f"Number {num} is Odd")
                
                # Using 'pass' statement as demonstration/placeholder
                if num == 0:
                    pass

            print(f"Sum of all numbers from {start} to {end} is: {total_sum}\n")
            break

        except ValueError:
            print("Invalid input! Please enter valid integers.\n")


def main():
    print("Welcome to the Pattern Generator and Number Analyzer!\n")
    
    while True:
        print("Select an option:")
        print("1. Generate a Pattern")
        print("2. Analyze a Range of Numbers")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            generate_pattern()
        elif choice == "2":
            analyze_numbers()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
