# NsySafePass

**NsySafePass** is a simple command line tool written in Python that helps you manage your passwords securely. It allows you to generate strong passwords, store them with your account information and retrieve them later when needed. All your passwords are stored in one file so you can access them at any time. The tool also checks the strength of your passwords and makes sure they are secure. It's a simple but handy tool for keeping track of all your passwords in one place, and you can use it right from the terminal.

Warm regards,

Naisya Aghis, the creator of this tool.

[![Follow on Instagram)](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/nsyaghis/)
[![Follow on LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nsyaghis/)
[![Follow on Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@nsyaghis)
[![Python Languange](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)](https://www.kali.org/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)

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
- Start: This takes you to the main features of this tool.
- About: Displays information about the tool.
- Exit: Exits the tool

After selecting "Start," you'll see options to add a new password, view all stored passwords, or search for a password by account name.

#### Add a new password
- Enter Account Name: Type the name of the account (e.g., "instagram") and press Enter.
- Enter Username: Type the username associated with the account and press Enter.
- Enter Password:
    - If you already have a password, type it and press Enter.
    - If you want the tool to generate a password, just press Enter without typing anything.
    - If you choose to generate a password, the tool will ask for your preferences:
        - Enter the desired password length
        - Indicate whether to include lowercase letters, uppercase letters, digits, and symbols by typing "y" (yes) or "n" (no) for each.
        - The tool will generate a password based on your preferences and show you its strength.
        - Confirm: If you're satisfied with the generated password, confirm by typing "y" (yes). If not, you can generate another one.
- The tool will show how strenght and store the password, username, and account name in the CSV file.

#### View all password
The tool will display all stored account names, usernames, and passwords on the screen.

#### Search for a password
- Enter Account Name: Type the name of the account you're looking for and press Enter.
- If the account is found, the tool will display the associated username and password. If not, it will tell you no entries were found.

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
![screenshot-1](https://github.com/user-attachments/assets/cf3e1722-259e-4c19-95ff-42258aed4a53)

# Enjoy your day!🌻
