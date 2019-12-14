import json


class StockPortfolio:

    def __init__(self, file):
        self.file = file
        self.stock_data = None
        with open(self.file, 'r') as f:
            self.stock_data = json.load(f)

    def stock_calculations(self):
        total = 0
        for item in self.stock_data["stock"]:
            print(f"\nStock Name :\t{item['stockname']}\nNumberof Shares :\t{item['numberofshares']}\n"
                  f"Price per Share:\t{item['shareprice']}")
            print(f"Total Stock Value of {item['stockname']}:\t{item['numberofshares']*item['shareprice']}\n")
            total += item['numberofshares']*item['shareprice']
        print(f"\nTotal Value of Stock Portfolio is :\t{total}")


if __name__ == "__main__":
    sp = StockPortfolio("stockportfolio.json")
    sp.stock_calculations()
