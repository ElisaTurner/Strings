# This program will check if a user input is a palindrome

# Define the main function
def main():
    while True:
        # Display an introduction
        print("Hello user! Are you ready to check some code!?\n")

        # Ask for a string
        user_input = input("Fantastic, now enter a string: ")
        print("We will be checking if it is a palindrome. A string spelled the same way forwards and backwards.\n")

        # Figure out user input backwards
        user_input_backwards = user_input[::-1]

        # Display the string check
        print(f"Is {user_input} the same as {user_input_backwards}? \n")

        if user_input == user_input_backwards:
            print("Yep, thats a palindrome! \n")
        else:
            print("No sorry, not a palindrome. \n")

        # Ask if user wants to continue
        another = input("Do you want to check another string? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == '__main__':
    main()

# This will prompt the user to enter a string and then print the result of the is_palindrome function.







