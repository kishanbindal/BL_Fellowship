import json
import datetime


class CompanyShares:

    def __init__(self, symbol=None, number_of_shares=None, transaction_time=None):
        self.symbol = symbol
        self.number_of_shares = number_of_shares
        self.transaction_time = transaction_time

    def get_transaction_time(self):
        self.transaction_time = datetime.datetime
        return self.transaction_time
    
    def gen_listing(self, file):
        listings = list()
        with open(file, 'r') as f:
            data = json.load(file)
            for item in data['company']:
                temp = CompanyShares(item['name'], item['shares'])
                item.append(temp)
        return listings
