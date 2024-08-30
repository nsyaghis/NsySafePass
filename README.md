# NsySafePass

**NsySafePass** is a simple command line tool written in Python that helps you manage your passwords securely. It allows you to generate strong passwords, store them with your account information and retrieve them later when needed. All your passwords are stored in one file so you can access them at any time. The app also checks the strength of your passwords and makes sure they are secure. It's a simple but handy tool for keeping track of all your passwords in one place, and you can use it right from the terminal.

Warm regards,

Naisya Aghis, the creator of this tool.


[![Follow on LinkedIn](https://img.shields.io/badge/Follow%20on%20LinkedIn-%230077B5.svg?style=social&logo=linkedin)](https://www.linkedin.com/in/nsyaghis/)

## How To Install

#### Clone this repository
```
git clone https://github.com/nsyaghis/nsysafepass.git
```

#### Enter the directory
```
cd nsysafepass
```
> [!IMPORTANT]  
> Make sure your operating system has already installed the latest version of python languange! See the documentation for how to install it: https://www.python.org/downloads/

#### Run it!
```
python ./src/nsysafepass.py
```

## How to use
After you run nsyaghis, you'll see the main menu with three options:
- Start: This takes you to the main features of this app.
- About: Displays information about the app.
- Exit: Exits the app

After selecting "Start," you'll see options to add a new password, view all stored passwords, or search for a password by account name.

#### Add a new password
- Enter Account Name: Type the name of the account (e.g., "instagram") and press Enter.
- Enter Username: Type the username associated with the account and press Enter.
- Enter Password:
    - If you already have a password, type it and press Enter.
    - If you want the app to generate a password, just press Enter without typing anything.
    - If you choose to generate a password, the app will ask for your preferences:
        - Enter the desired password length
        - Indicate whether to include lowercase letters, uppercase letters, digits, and symbols by typing "y" (yes) or "n" (no) for each.
        - The app will generate a password based on your preferences and show you its strength.
        - Confirm: If you're satisfied with the generated password, confirm by typing "y" (yes). If not, you can generate another one.
- The app will show how strenght and store the password, username, and account name in the CSV file.

#### View all password
The app will display all stored account names, usernames, and passwords on the screen.

#### Search for a password
- Enter Account Name: Type the name of the account you're looking for and press Enter.
- If the account is found, the app will display the associated username and password. If not, it will tell you no entries were found.

#### Back to main menu
This option will take you to the main menu.

## Needs Updated Below
### Imports
The following modules were used in this script:
- csv
- os
- random
- string
- re
- getpass

### Usage 
__Python 2.7.x__
python 

__Python 3__
python3 

## Sample Screenshots
![nsysafepass](https://github.com/user-attachments/assets/145f2521-c3d6-44e7-889b-39e8061a7c82)


# Enjoy your day!🌻
