# You are given a string s containing only lowercase English letters,
# and an integer k. You need to encrypt the string using a Caesar Cipher
# with a shift of k.

# The Caesar Cipher works by shifting each letter in the string by a
# fixed number of positions down the alphabet. For example, with a shift of
# k = 3, 'a' would be encrypted to 'd', 'b' to 'e', 'c' to 'f', and so on.

# Return the encrypted string.

# Define the main function
def main():
    while True:
        # Display an introduction
        print("Welcome to the Caesar Cipher Encryptor!\n")
        print("Give me a number to shift by!\n")

        # Prompt for shift number
        shift_number = int(input("Please enter a number: "))  # Convert input to integer

        # Prompt for string
        shift_string = input("Please enter a string: ").lower() 
        
        # Display the string and shift number
        print(f"Shift number: {shift_number} and String: {shift_string} \n")

        # Shift the string by shift number
        new_string = shift_string_by_number(shift_string, shift_number)

        # Print the encrypted string
        print(f"Encrypted string: {''.join(new_string)}\n")

        # Ask if user wants to continue
        another = input("Do you want to do another string and shift? (yes/no): ").lower()
        if another != 'yes':
            break

def shift_string_by_number(s, k):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    new_key = k % 25
    new_string = []

    for char in s:
        if char.isalpha():
            index = alphabet.index(char)
            new_index = (index + new_key) % 26
            new_char = alphabet[new_index]
            new_string.append(new_char)
        else:
            new_string.append(char)

    return new_string

if __name__ == '__main__':
    main()
