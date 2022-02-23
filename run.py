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
    Run a while loop to collect the valid month from the user via the terminal,
    which must be from month 1 to 12. The loop will repeatedly request a valid
    data until the data collected is correct.
    """

    while True:
        print("Welcome to Wedding Savings Planner.\n"),
        print("Please state the month in terms of a number"),
        print("You may choose from 1 to 12.\n"),
        print("Example: If it is February, you should state 2\n")

        month = input("Enter the month here:\n")
        if validate_data(month):
            print("Month has been noted, thank you.\n")
            show_alldata_month1(month)
            show_alldata_month2(month)
            break


def validate_data(values):

    """
    Raises ValueError if the month
    selected is not a valid number or not an integer.
    """

    try:
        if int(values) <= 0:

            raise ValueError
            f'{"You may only choose from month 1 to 12"}'

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    try:
        if int(values) > 12:

            raise ValueError
            f'{"You may only choose from month 1 to 12"}'

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def show_alldata_month1(month):

    """
    Projects the chosen month, expenses, and savings for
    January
    """
    print("Retrieving data...\n")

    if month == "1":
        alldata_m1_1 = SHEET.worksheet("all_data").get('A1')[0][0]
        alldata_m1_2 = SHEET.worksheet("all_data").get('B2')[0][0]
        print(("The month you have chosen : "), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("all_data").get('B3')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)
        
        print("\n")
        print("Retrieving savings data...\n")

        jan = int(alldata_m1_3)
        print(("Your savings for this month will be:"), jan)

        jan = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), jan)

    return month


def show_alldata_month2(month):

    """
    Projects expenses,savings and balance for
    February
    """

    if month == "2":
        alldata_m1_1 = SHEET.worksheet("all_data").get('A5')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("all_data").get('B6')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)
        
        alldata_m1_3 = SHEET.worksheet("all_data").get('B7')[0][0]
        print("\n")
        print("Retrieving total savings...\n")

        feb = int(alldata_m1_3)
        print(("Your savings for this month will be:"), feb)
    
        """
        Projects savings after deduction of expenses
        """

        feb = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), feb)

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """

        alldata_m1_4 = SHEET.worksheet("all_data").get('B3')[0][0]
        feb_ts = int(alldata_m1_3) + int(alldata_m1_4)
        print(("Your total savings before expenses year to date is:"), feb_ts)

    return month


def main():

    """
    Run all program functions
    """
    get_month_data()


main()
