"""
    @Summary Driver Code for StockAccount.py

    @Author Kishan Bindal

    @Since December 2019
"""
from oop import stockaccount


def drive_account():
    sa = stockaccount.StockAccount("stockdetails.json") # Initialize Stock portfolio
    print("Welcome to your Stock Portfolio \n")
    print("\t Menu")
    print("1. Buy Shares\n2. Sell Shares\n3. Save Transaction\n4. Print Report\n5. Exit\n")
    while True:
        user_choice = int(input("Please choose from above options. Enter 1-5 :\n"))  # take in user choice
        if user_choice not in range(1, 6):
            raise ValueError("Enter Numbers between 1-5 only!")  # raise error when value not in range of options
        else:
            if user_choice == 1:
                sa.buy()
                print(sa.get_transaction_time())
            elif user_choice == 2:
                sa.sell()
                print(sa.get_transaction_time())
            elif user_choice == 3:
                sa.save_file()
            elif user_choice == 4:
                sa.print_report()
            else:
                break


if __name__ == '__main__':
    drive_account()
