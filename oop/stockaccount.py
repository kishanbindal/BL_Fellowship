"""
    @Summary Stock Account Portfolio for customer

    @Author Kishan Bindal

    @Since December 2019
"""
from oop import companyshares
import json


class StockAccount(companyshares.CompanyShares):

    def __init__(self, file):
        companyshares.CompanyShares.__init__(self)
        self.file = file
        self.account = self.stock_account()  # get account data from json file
        self.company_listings = companyshares.CompanyShares.gen_comp(self)  # generate list of company objects

    def stock_account(self):  # get account data from json file
        with open(self.file, 'r') as f:
            data = json.load(f)
        return data

    def value_of(self):  # Get total Value of Portfolio
        total = 0
        for item in self.account['stock']:
            total += item["numberofshares"] * item["shareprice"]
        return total

    def buy(self):  # Buy Shares
        print("Available Stocks :\n\nStock Name \t\tNumber\t\tPrice/Share\n")
        for comp_obj in self.company_listings:
            print(f"{comp_obj.symbol}\t\t\t{comp_obj.number_of_shares}\t\t{comp_obj.price}")
        user_input = input("\nPlease enter which stock you would like to buy? \n")
        in_file = False  # Used as a True/False switch(if company does exist, aids in creating new company object
        for comp_obj in self.company_listings:
            for user_stock in self.account['stock']:
                # Checking for company to be in both json files
                if (user_input == comp_obj.symbol) and (user_input == user_stock['stockname']):
                    user_share = int(input("Number of Shares You would like to purchase? :\t"))
                    if user_share > comp_obj.number_of_shares:
                        print("Transaction Not Possible since company does not have enough shares to sell")
                    else:
                        user_stock['numberofshares'] += user_share  # add stocks to user
                        comp_obj.number_of_shares -= user_share  # Reduce stocks available in company
                        comp_obj.get_transaction_time()  # Transaction time of the operation
                        print(f"\nTransaction time ===> {comp_obj.transaction_time}\n")
                        print("==============Company============")
                        print(f"{comp_obj.symbol}\t\t\t{comp_obj.number_of_shares}\t\t{comp_obj.price}")
                        print("==============Customer============")
                        print(f"{user_stock['stockname']}\t\t\t{user_stock['numberofshares']}")
                        in_file = True
                        break

        if in_file is False:  # If company name does not exist, create new company object
            n = input("\nEnter Name of Company :")
            ns = int(input("\nEnter Number of shares the company has to sell :"))
            pps = float(input("\nEnter Price Per Share :"))
            self.company_listings.append(companyshares.CompanyShares(n, ns, pps))  # Add company obj to company listings
            temp = self.company_listings[-1]
            user_share = int(input("Number of Shares You would like to purchase? :\t"))
            if user_share > temp.number_of_shares:
                print(f"Transaction not possible since Company does not have enough shares to sell")
            else:
                data = dict()
                data['stockname'] = n
                data['numberofshares'] = user_share
                data['shareprice'] = pps
                temp.number_of_shares -= user_share
                temp.get_transaction_time()
                self.account['stock'].append(data)  # Add company and shares to user's portfolio
                test = self.account['stock'][-1]  # Used temp var for displaying Transaction details
                print(f"Transaction time ====> {temp.transaction_time}")
                print("==============Company============")
                print(f"{temp.symbol}\t\t\t{temp.number_of_shares}\t\t{temp.price}")
                print("==============Customer============")
                print(f"{test['stockname']}\t\t\t{test['numberofshares']}")

    def sell(self):  # Sell stocks to company, if company not present in list, add company to list
        print("Customer Portfolio :\n\nStock Name \t\tNumber\t\tPrice/Share\n")  # Displaying customers Portfolio
        for item in self.account['stock']:
            print(f"{item['stockname']}\t\t\t{item['numberofshares']}\t\t\t{item['shareprice']}")
        user_sell = input("\nPlease Enter which Company Stock you would like to sell? \n")
        in_file = False  # Switch case True/False
        for comp_obj in self.company_listings:
            for user_stock in self.account['stock']:
                # checking for company name in both json files
                if (user_sell == comp_obj.symbol) and (user_sell == user_stock['stockname']):
                    sell_num = int(input("Number of Shares You would like to Sell? :\t"))  # Number of stocks to sell
                    # If no. of shares>available shares then transaction not possible
                    if sell_num > user_stock['numberofshares']:
                        print("Transaction Not Possible since You do not have enough shares to sell")
                    else:
                        user_stock['numberofshares'] -= sell_num  # Update User stocks
                        comp_obj.number_of_shares += sell_num  # Update company stocks
                        comp_obj.get_transaction_time()
                        print(f"\nTransaction time ===> {comp_obj.transaction_time}\n")  # Display Transaction Details
                        print("==============Company============")
                        print(f"{comp_obj.symbol}\t\t\t{comp_obj.number_of_shares}\t\t{comp_obj.price}")
                        print("==============Customer============")
                        print(f"{user_stock['stockname']}\t\t\t{user_stock['numberofshares']}")
                        in_file = True
                        break
        if in_file is False:  # If company doesnt exist, create company object for user
            n = input("\nEnter Name of Company :")
            ns = int(input("\nEnter Number of shares you have to sell :"))
            pps = float(input("\nEnter Price Per Share :"))
            data = dict()
            data['stockname'] = n
            data['numberofshares'] = ns
            data['shareprice'] = pps
            self.account['stock'].append(data)  # add company to customer's portfolio
            temp = self.account["stock"][-1]
            sell_share = int(input("\nEnter Number of shares you want to sell : "))  # no of shares to sell
            if sell_share > self.account["stock"][-1]['numberofshares']:
                print('Transaction Incomplete : You do not have enough shares to sell')
            else:
                self.account['stock'][-1]['numberofshares'] -= sell_share  # Update number of shares for user
                self.company_listings.append(companyshares.CompanyShares(n, sell_share, pps))
                test = self.company_listings[-1]
                test.get_transaction_time()
                print(f"\nTransaction time ===> {test.transaction_time}\n")  # Display Transaction details
                print("==============Company============")
                print(f"{test.symbol}\t\t\t{test.number_of_shares}\t\t{test.price}")
                print("==============Customer============")
                print(f"{temp['stockname']}\t\t\t{temp['numberofshares']}")

    def save_file(self):  # Save Changes to customer and company json files
        with open(self.file, 'r+') as f:
            print("\nSaving User's Stock Account Details\n")
            json.dump(self.account, f, indent=2)  # add changes to customer's portfolio json file
        test = []
        for company in self.company_listings:  # Adding company listing into test[]
            temp = dict()
            temp['name'] = company.symbol
            temp['numberofshares'] = company.number_of_shares
            temp['shareprice'] = company.price
            test.append(temp)
        temp = dict()
        temp['company'] = test  # Making dictionary in order to save to json file
        companyshares.CompanyShares.save(temp)  # Saving changed to Company's json file

    def print_report(self):  # Printing Report of Customer's Portfolio
        print("\nCustomer Stock Account :\n")
        print("Company Name\t\tNumber of Shares\t\tPrice/Share\t\tValue of Share in company")
        for stock in self.account['stock']:
            print(f"{stock['stockname']}\t\t\t\t\t\t{stock['numberofshares']}\t\t\t\t{stock['shareprice']}\t\t\t"
                  f"{stock['numberofshares'] * stock['shareprice']}")
        print(f"\nTotal Value of Portfolio :\t\t\t\t\t\t\t\t\t{self.value_of()}")
