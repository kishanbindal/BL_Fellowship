from oop import companyshares
import json


class StockAccount(companyshares.CompanyShares):

    def __init__(self, file):
        companyshares.CompanyShares.__init__(self)
        self.file = file
        self.account = self.stock_account()
        self.company_listings = list()

    def get_listings(self):
        self.company_listings = companyshares.CompanyShares.gen_listing(self.file)

    def stock_account(self):
        with open(self.file, 'r') as f:
            data = json.load(f)
        return data

    def value_of(self):
        total = 0
        for item in self.account['stock']:
            total += item["numberofshares"] * item["shareprice"]
        print(f"Total value of stocks in Account :\t\t{total}")
        return total

    def buy(self):
        pass
