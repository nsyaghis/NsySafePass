import csv
import os
import random
import string
import re
from getpass import getpass

CSV_FILE = 'passwords.csv'

# Siapin file CSV
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Account', 'Username', 'Password'])

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

        if use_uppercase:
            characters += characters.upper()

    if not characters:
        raise ValueError("No character types selected!")

    return ''.join(random.choice(characters) for _ in range(length))

# Password Manager
def add_password(account, username, password=None):
    if password is None:
        # Generate password 
        while True:
            print("\nPassword Generator")
            length = int(input("Enter the desired password length: "))
            use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Include digits? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

            generated_password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
            print(f"Generated Password: {generated_password}")

            # Check password strength
            strength = check_password_strength(generated_password)
            print(f"\nGenerated Password Strength: {strength}")

            confirm = input("\nDo you want to use this generated password? (y/n): ").lower()
            if confirm == 'y':
                break
            else:
                print("Please generate another password.")

        password = generated_password

    # Check custom password strength 
    if password:
        strength = check_password_strength(password)
        print(f"\nCustom Password Strength: {strength}")

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([account, username, password])

    print(f"\nPassword for {account} added successfully.")

     # Biar ga langsung diclear
    input("\nPress Enter to continue...")

# Liat Password
def view_passwords():
    try:
        display_header()
        print("\n")

        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"Account: {row['Account']}, Username: {row['Username']}, Password: {row['Password']}")

    except Exception as e:
        print(f"Error viewing passwords: {e}")

# Cari Password
def search_password(account):
    try:
        display_header()
        print("\n")

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
        print(f" - {criterion.capitalize()}: {status}")

    return strength

# Bersihin Terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display Header
def display_header():
    clear_terminal()
    # print("\n")
    print("""
  _  _         ___        __     ___            
 | \| |____  _/ __| __ _ / _|___| _ \__ _ ______
 | .` (_-< || \__ \/ _` |  _/ -_)  _/ _` (_-<_-<
 |_|\_/__/\_, |___/\__,_|_| \___|_| \__,_/__/__/
          |__/                                  
    """)

                                                                                                                            
    print("\nNsySafePass ")
    print("-------------------------")

# About
def display_about():
    display_header()
    print("\nAbout\n")
    print("NsySafePass is a homemade password manager tool written in Python.")
    print("This tool has 3 main features: password manager, password generator,")
    print("and password strength checker. Hope you like it!")
    print("\nWarm regards, \n\nNaisya Aghis, the creator of this app.\n")

    # Biar ga langsung diclear
    input("Press Enter to continue...")

    clear_terminal()
    display_header()

# Main
def main():
    init_csv()

    while True:
        display_header()
        print("\nMain Menu\n")
        print("1. Start")
        print("2. About")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_header()
            while True:
                clear_terminal()
                display_header()
                print("\nPassword Manager\n")
                print("1. Add a new password")
                print("2. View all passwords")
                print("3. Search for a password")
                print("4. Back to Main Menu")

                sub_choice = input("Choose an option: ")

                if sub_choice == '1':
                    account = input("\nEnter the account name: ")
                    username = input("Enter the username: ")

                    while True:
                        try:
                            password = getpass("Enter the password (or press Enter to generate): ")
                            if len(password) < 8:
                                raise ValueError
                            break
                        except ValueError:
                            print("Password must be at least 8 characters long. Generating a new password instead.")
                            length = int(input("Enter the desired password length: "))
                            use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
                            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
                            use_digits = input("Include digits? (y/n): ").lower() == 'y'
                            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

                            generated_password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
                            print(f"\nGenerated Password: {generated_password}")

                            # Check password strength
                            strength = check_password_strength(generated_password)
                            print(f"\nGenerated Password Strength: {strength}")

                            confirm = input("\nDo you want to use this generated password? (y/n): ").lower()
                            if confirm == 'y':
                                password = generated_password
                                break
                            else:
                                print("Please generate another password.")

                    if password:
                        strength = check_password_strength(password)
                        print(f"\nCustom Password Strength: {strength}")

                    add_password(account, username, password)

                elif sub_choice == '2':
                    view_passwords()
                    input("\nPress Enter to continue...")

                elif sub_choice == '3':
                    account = input("Enter the account name to search: ")
                    search_password(account)
                    input("\nPress Enter to continue...")

                elif sub_choice == '4':
                    break

                else:
                    print("Invalid option, please try again.")

        elif choice == '2':
            display_about()

        elif choice == '3':
            display_header()
            print("Exiting the program.")
            break

        else:
            display_header()
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()