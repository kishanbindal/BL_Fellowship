"use strict";
var fs = require('file-system');
var rl = require('readline-sync');
class ShareHolder {
    constructor() {
        this.stock_list = this.getCustomerStockList();
    }
    readFile() {
        let file = fs.readFileSync('customerstockportfolio.json', 'utf8');
        return JSON.parse(file);
    }
    getCustomerStockList() {
        let file = this.readFile();
        let result = [];
        for (var data in file['stock']) {
            let share_details = file['stock'][data];
            result.push(share_details);
        }
        return result;
    }
    valueOf() {
        let portfolio_value = 0;
        for (var i = 0; i < this.stock_list.length; i++) {
            let amt = this.stock_list[i]['shareprice'] * this.stock_list[i]['numberofshares'];
            portfolio_value += amt;
        }
        console.log(`Total Share Holder Portfolio Value Is: ${portfolio_value}`);
    }
}
class CompanyListing {
    constructor() {
        this.company_listings = this.getCompanyListings();
    }
    readFile() {
        let file = fs.readFileSync('companylistings.json', 'utf8');
        return JSON.parse(file);
    }
    getCompanyListings() {
        let file = this.readFile();
        let result = [];
        for (var i in file['company']) {
            let company_share = file['company'][i];
            result.push(company_share);
        }
        return result;
    }
    addListing(company_name, numberofshares, shareprice) {
        let company_details = {
            "name": company_name,
            "numberofshares": numberofshares,
            "shareprice": shareprice
        };
        this.company_listings.push(company_details);
    }
}
class StockAccount {
    constructor() {
        this.owner = new ShareHolder();
        console.log(this.owner.stock_list);
        this.company = new CompanyListing();
        console.log(this.company.company_listings);
    }
    valueOf() {
        return this.owner.valueOf();
    }
    checkForCompany(stockname) {
        let data = this.company.company_listings;
        for (var i = 0; i < data.length; i++) {
            if (stockname == data[i]['name']) {
                return true;
            }
        }
        return false;
    }
    getShareIndex(stockname) {
    }
}
let sa = new StockAccount();
// sa.buyShares();
