"""
    @Summary Company Shares class for stock Account

    @Author Kishan Bindal

    @Since December 2019
"""
import json
import datetime


class CompanyShares:
    # Class variable data to stored json file data
    with open("companylisting.json", 'r') as f:
        data = json.load(f)

    def __init__(self, symbol=None, number_of_shares=None, price=None):
        self.symbol = symbol  # variable to take company name
        self.number_of_shares = number_of_shares  # Variable to take number of shares company has
        self.price = price  # variable for price of each share
        self.transaction_time = None

    def get_transaction_time(self):  # Function to get transaction time when we buy or sell shares
        self.transaction_time = datetime.datetime.now()
        return self.transaction_time

    def gen_comp(self):  # Generating a list of company objects
        listings = list()
        for item in self.data['company']:
            listings.append(CompanyShares(item['name'], item['numberofshares'], item['shareprice']))
        return listings

    @staticmethod
    def save(dat):  # Method to Save data into json file
        with open("companylisting.json", 'w') as f:
            json.dump(dat, f, indent=2)  # Saving Data to json file
