# Coursework Assessment 1
# Name: Md Mostak Laheri
# Student No: 2511809

# A Caesar Cipher Program
import os.path

def welcome():
    print('Welcome to the Caesar Cipher')
    print('This program encrypts and decrypts text with the Caesar Cipher. ')
    return


def enter_message():
    mode = ''
    message = ''
    shift = 0
    while True:
        mode = input('would you like to encrypt (e) or decrypt (d):')
        if mode == 'e' or mode == 'd':
            message = input('what message would you like to encrypt:')
            message = message.upper()
            while True:
                shift = input('what is the shift number:')
                if shift.isdigit():
                    shift_num = int(shift)
                    if shift_num >0 and shift_num<26:
                         return (mode, message, shift_num)
                print('invalid shift. Enter a valid shift number!')
        print('invalid mode')
    return (mode, message, shift)


def encrypt(message,shift):
    message = message.upper()
    new_message=''

    print('The message to encrypt is', message)

    for ch in message:
        if ch.isalpha():
            new_code=ord(ch)+shift
            #print(new_code)

            if new_code>90:
                new_code =(ord(ch)-26)+shift
                #print(new_code)
                new_message+=chr(new_code)
            else:
                new_message+=chr(new_code)
        else:
            new_message+=ch
            #print(new_message)
    return new_message


def decrypt(message,shift):
    
    message = message.upper()
    new_message = ""

    for ch in message:
        if ch.isalpha():
            new_code = ord(ch) - shift
            if new_code < 65:
                new_code += 26
            new_message += chr(new_code)
        else:
            new_message += ch

    return new_message

def process_file(filename, mode,shift):
    list_messages = []
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if mode == 'e':
                    encrypted_line = encrypt(line, shift)
                    list_messages.append(encrypted_line)
                elif mode== 'd':
                    decrypted_line = decrypt(line, shift)
                    list_messages.append(decrypted_line)
                else:
                    print("The file '{filename}' does not exist. Please enter a valid filename!")
            return list_messages


def write_messages(lines):
    with open("results.txt", 'w') as file:
        for line in lines:
            file.write(line + '\n')
    print("Ok Done!, The messages have been written to results.txt.")
    return


def is_file(filename):
    return os.path.isfile(filename)
    return False


def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)?: ").lower()
        if mode not in ['e', 'd']:
            print("Invalid mode. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        input_type = input("Would you like to process using the message (c) or a file (f)?: ").lower()

        if input_type == 'c':
            message = input("Enter the message you would like to process: ")
            shift = input("Choose the shift number from 1 to 25: ")
            if shift.isdigit() and 0 < int(shift) < 26:
                return mode, message, None, int(shift)
            else:
                print("Invalid shift number. Please choose any number from 1 to 25.")

        elif input_type == 'f':
            filename = input("Enter the filename to process: ")
            while not is_file(filename):
                print(f"File named '{filename}' not found. Please try again.")
                filename = input("Please enter a valid filename to process: ")

            shift = input("Choose the shift number from 1 to 25: ")
            if shift.isdigit() and 0 < int(shift) < 26:
                return mode, None, filename, int(shift)
            else:
                print("Invalid shift number. Please choose any number from 1 to 25.")

        else:
            print("Invalid input. Please enter 'c' for message or 'f' for file.")

    return (mode, message, filename, shift)
    
"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encrypt (e) or decrypt (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encrypt/decrypt.
    • encrypt/decrypt the message as appropriate and print the output.
    • Prompt the user whether they would like to encrypt/decrypt another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.
"""
def main():
    welcome()
    while True:
        mode, message, filename, shift = message_or_file()

        if filename:
            # Process the file if filename is provided
            results = process_file(filename, mode, shift)
            for line in results:
                print(line)
            save_to_file = input("Do you like to save the processed output to a file? Yes (y) or No (n): ").lower()
            if save_to_file == 'y':
                write_messages(results)
        else:
            # Process a single message if no filename is provided
            if mode == 'e':
                result = encrypt(message, shift)
                print("Encrypted message:", result)
            else:
                result = decrypt(message, shift)
                print("Decrypted message:", result)

        repeat = input("Would you like to process another text or file? (y/n): ").lower()
        if repeat != 'y':
            print("Thank you! goodbye")
            break
    return


# Program execution begins here
if __name__ == '__main__':
    main()
