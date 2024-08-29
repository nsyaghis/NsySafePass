import csv
import os
import random
import string
import re
from getpass import getpass

CSV_FILE = 'passwords.csv'

# Initialize CSV file
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Account', 'Username', 'Password'])

# Display Header Function
def display_header():
    clear_terminal()
    print("\n")
    print("-------------------------")
    print("""

  _  _         ___        __     ___            
 | \| |____  _/ __| __ _ / _|___| _ \__ _ ______
 | .` (_-< || \__ \/ _` |  _/ -_)  _/ _` (_-<_-<
 |_|\_/__/\_, |___/\__,_|_| \___|_| \__,_/__/__/
          |__/                                  

    """)

                                                                                                                            
    print("\n\nNsySafePass ")
    print("\nNaisya Aghis Nabila")
    print("-------------------------")

# About
def display_about():
    display_header()
    print("\nAbout\n")
    print("NsySafePass is a homemade password manager tool written in Python.")
    print("This tools has 3 main features: password manager, password generator, and password strength checker. Hope you like it!")
    print("\nWarm regards, \n\nNsyaghis, the creator of this app.\n")

    # Pause to keep the screen visible
    input("Press Enter to continue...")

# Main Menu Function
def main_menu():
    print("\nMain Menu")
    print("1. Password Generator")
    print("2. Password Manager")
    print("3. Password Strength Checker")
    print("4. About")
    print("5. Exit")

# Password Generator
def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True, mode='all'):
    characters = ''
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # if mode == 'easy_to_read':
    #     characters = characters.replace('l', '').replace('I', '').replace('1', '').replace('0', '').replace('O', '')
    # elif mode == 'easy_to_say':
    #     vowels = 'aeiou'
    #     consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    #     characters = consonants + vowels
    #     if use_uppercase:
    #         characters += characters.upper()

    if not characters:
        raise ValueError("No character types selected!")

    return ''.join(random.choice(characters) for _ in range(length))

# Password Manager
def add_password(account, username, password):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([account, username, password])
    print(f"Password for {account} added successfully.")

def view_passwords():
    try:
        clear_terminal()  # Clear terminal before displaying passwords
        display_header()  # Display header
        
        print("\n")  # Add newline after header
        
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"Account: {row['Account']}, Username: {row['Username']}, Password: {row['Password']}")
        
        print("\n")  # Add newline after password list
        
        print("Password Manager Options:")
        print("1. Add a new password")
        print("2. View all passwords")
        print("3. Search for a password")
        print("4. Back to Main Menu")
        
    except Exception as e:
        print(f"Error viewing passwords: {e}")

def search_password(account):
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            matching_accounts = []
            for row in reader:
                if row['Account'].lower() == account.lower():
                    matching_accounts.append({
                        'Account': row['Account'],
                        'Username': row['Username'],
                        'Password': row['Password']
                    })
            if matching_accounts:
                print("Found Accounts:")
                for account_info in matching_accounts:
                    print(f"Account: {account_info['Account']}, Username: {account_info['Username']}, Password: {account_info['Password']}")
            else:
                print("No entries found for that account.")
    except Exception as e:
        print(f"Error searching passwords: {e}")

# Password Strength Checker
def check_password_strength(password):
    strength_criteria = {
        'length': len(password) >= 8,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'digit': re.search(r'\d', password) is not None,
        'special_char': re.search(r'[@#$%^&*(),.?":{}|<>]', password) is not None,
    }
    
    strength_score = sum(strength_criteria.values())
    
    if strength_score <= 2:
        strength = "Weak"
    elif strength_score == 3:
        strength = "Medium"
    elif strength_score >= 4:
        strength = "Strong"
    
    print("\nPassword Strength Check:")
    print(f"Password: {password}")
    print(f"Strength: {strength}\n")
    print("Criteria met:")
    for criterion, met in strength_criteria.items():
        status = "Yes" if met else "No"
        print(f"  - {criterion.capitalize()}: {status}")
    
    return strength

# Clear Terminal Function
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main Program Loop
def main():
    init_csv()
    
    while True:
        display_header()  # Ensure header is displayed
        
        main_menu()
        
        choice = input("Choose an option: ")

        if choice == '1':
            display_header()
            
            print("\nPassword Generator")
            
            while True:
                try:
                    length = int(input("Enter the desired password length: "))
                    if length < 1:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid length. Please enter a positive integer.")
            
            use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Include digits? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            
            # while True:
            #     mode = input("Choose mode (all/easy_to_read/easy_to_say): ").lower()
            #     if mode in ['all', 'easy_to_read', 'easy_to_say']:
            #         break
            #     else:
            #         print("Invalid mode. Please choose from 'all', 'easy_to_read', or 'easy_to_say'.")
            
            password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
            print(f"\nGenerated Password: {password}")

            input("\nPress Enter to continue...")

        
        elif choice == '2':
            display_header()
            
            print("\nPassword Manager")
            
            while True:
                print("1. Add a new password")
                print("2. View all passwords")
                print("3. Search for a password")
                print("4. Back to Main Menu")
                
                sub_choice = input("Choose an option: ")

                if sub_choice == '1':
                    account = input("Enter the account name: ")
                    username = input("Enter the username: ")
                    while True:
                        try:
                            password = getpass("Enter the password: ")
                            if len(password) < 8:
                                raise ValueError
                            break
                        except ValueError:
                            print("Password must be at least 8 characters long.")
                    
                    add_password(account, username, password)
                elif sub_choice == '2':
                    view_passwords()
                elif sub_choice == '3':
                    account = input("Enter the account name to search: ")
                    search_password(account)
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid option, please try again.")
        
        elif choice == '3':
            display_header()
            
            print("\nPassword Strength Checker")
            
            while True:
                try:
                    password = input("Enter a password to check its strength: ")
                    if len(password) < 8:
                        raise ValueError
                    break
                except ValueError:
                    print("Password must be at least 8 characters long.")
            
            check_password_strength(password)

        elif choice == '4':
            display_about()  # Show the about information
            
        elif choice == '5':
            display_header()
            
            print("Exiting the program.")
            break
        
        else:
            display_header()
            
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
