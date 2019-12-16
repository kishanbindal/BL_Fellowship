"""
    @Summary To Display Stock value of customer Stock Portfolio

    @Author Kishan Bindal

    @Since December 2019
"""
import json


class StockPortfolio:

    def __init__(self, file):  # Initialise instance variable for stockportfolio obj
        self.file = file
        self.stock_data = None
        with open(self.file, 'r') as f:
            self.stock_data = json.load(f)  # Set stock data from file

    def stock_calculations(self):  # Calculate Value of stocks in each company and total Portfolio Value
        total = 0
        for item in self.stock_data["stock"]:
            print(f"\nStock Name :\t{item['stockname']}\nNumberof Shares :\t{item['numberofshares']}\n"
                  f"Price per Share:\t{item['shareprice']}")
            print(f"Total Stock Value of {item['stockname']}:\t{item['numberofshares']*item['shareprice']}\n")
            total += item['numberofshares']*item['shareprice']
        print(f"\nTotal Value of Stock Portfolio is :\t{total}")


# Driver code for above Code
if __name__ == "__main__":
    sp = StockPortfolio("stockportfolio.json")
    sp.stock_calculations()
