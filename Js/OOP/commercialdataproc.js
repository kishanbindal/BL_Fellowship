var fs = require('file-system');
var rl = require('readline-sync');
var ShareHolder = /** @class */ (function () {
    function ShareHolder() {
        this.stock_list = this.getCustomerStockList();
    }
    ShareHolder.prototype.readFile = function () {
        var file = fs.readFileSync('customerstockportfolio.json', 'utf8');
        return JSON.parse(file);
    };
    ShareHolder.prototype.getCustomerStockList = function () {
        var file = this.readFile();
        var result = [];
        for (var data in file['stock']) {
            var share_details = file['stock'][data];
            result.push(share_details);
        }
        return result;
    };
    ShareHolder.prototype.valueOf = function () {
        var portfolio_value = 0;
        for (var i = 0; i < this.stock_list.length; i++) {
            var amt = this.stock_list[i]['shareprice'] * this.stock_list[i]['numberofshares'];
            portfolio_value += amt;
        }
        console.log("Total Share Holder Portfolio Value Is: " + portfolio_value);
    };
    return ShareHolder;
}());
var CompanyListing = /** @class */ (function () {
    function CompanyListing() {
        this.company_listings = this.getCompanyListings();
    }
    CompanyListing.prototype.readFile = function () {
        var file = fs.readFileSync('companylistings.json', 'utf8');
        return JSON.parse(file);
    };
    CompanyListing.prototype.getCompanyListings = function () {
        var file = this.readFile();
        var result = [];
        for (var i in file['company']) {
            var company_share = file['company'][i];
            result.push(company_share);
        }
        return result;
    };
    CompanyListing.prototype.addListing = function (company_name, numberofshares, shareprice) {
        var company_details = {
            "name": company_name,
            "numberofshares": numberofshares,
            "shareprice": shareprice
        };
        this.company_listings.push(company_details);
    };
    return CompanyListing;
}());
var StockAccount = /** @class */ (function () {
    function StockAccount() {
        this.owner = new ShareHolder();
        console.log(this.owner.stock_list);
        this.company = new CompanyListing();
        console.log(this.company.company_listings);
    }
    StockAccount.prototype.valueOf = function () {
        return this.owner.valueOf();
    };
    StockAccount.prototype.checkForCompany = function (stockname) {
        var data = this.company.company_listings;
        for (var i = 0; i < data.length; i++) {
            if (stockname == data[i]['name']) {
                return true;
            }
        }
        return false;
    };
    StockAccount.prototype.buyShares = function () {
        var stock_name = rl.question("Enter company name whose shares you would like to buy? :");
        var number_of_shares = parseInt(rl.question("Enter Number of Stocks"));
        if (this.checkForCompany(stock_name)) {
            var company_list = this.company.company_listings;
            for (var i = 0; i < company_list.length; i++) {
                if (number_of_shares < this.company[i]['numberofshares']) {
                }
            }
        }
    };
    return StockAccount;
}());
var sa = new StockAccount();
sa.buyShares();
