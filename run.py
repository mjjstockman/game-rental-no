# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Dependencies for google sheets
import gspread
from google.oauth2.service_account import Credentials

# IAM specifiying user access
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("game_rental")

# sales = SHEET.worksheet("games")
# data = sales.get_all_values()
# print(data)

def choose_action():
    """
    Display initial options to user.
    Get desiered action input from user via the terminal.
    """
    print("Do you want to:\n 1) Make a sale?\n 2) Return a sale?\n "
          "3) Check stock?\n 4) Add a new customer?\n 5) Add a new title?\n")

    chosen_action = input("Please select from above by entering the "
                          "corresponding number and pressing Enter: ")
    
    print(chosen_action)


choose_action()
