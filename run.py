import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('wedding-savings')


def get_month_data():

    """
    Get month from the user.

    """
    print("Welcome to Wedding Savings Planner.\n")
    print("Please state the month in terms of a number"),
    print("You may choose from 1 to 12.\n"),
    print("Example: If it is February, you should state 2\n")

    month = input("Enter the month here:\n")


def main():

    """
    Run all program functions
    """
    get_month_data()


main()
