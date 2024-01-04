import phoney
import csv

def present_menu():
  # TODO: Write a function that asks the user if they want to search for a (F) phone number, (A) area code, (E) exchange, or (X) exit
  print("Please choose from the following options: ")
  print("F: Search for full phone number")
  print("A: Search for area code")
  print("E: Search for an exchange")
  print("X: Exit the program")


def main():
    # TODO: Import CSV file as Python list
    filename = 'phone_numbers(1).csv'
    numbers = []
    with open(filename, 'r') as f:
        # Create an iterable element that will hold the contents of the CSV file
        reader = csv.reader(f)
        # Loop through the reader and extend the list with values
        for row in reader:
            numbers.extend(row)
    # TODO: Report to the user how many numbers were in the original list
    print(f"There are {len(numbers)} phone numbers in the CSV file")
    # TODO: Use the `phoney.clean_phone_numbers` function to return a list of valid, digit-only phone numbers
    clean = phoney.clean_phone_numbers(numbers)
    # TODO: Start a loop that allows the user to search the phone number data
    while True:    
        present_menu()
        choice = input("Enter your selection: ").upper()
        if choice == 'F':
           search_term = input("Please enter the digits to search: ")
           phoney.find_number(clean, search_term)
        elif choice == 'A':
           search_term = input("Please enter the digits to search: ")
           phoney.find_areacode(clean, search_term)
        elif choice == 'E':
           search_term = input("Please enter the digits to search: ")
           phoney.find_exchange(clean, search_term)
        elif choice == 'X':
           print("Good bye!")
           break


if __name__== "__main__":
  main()