var fs = require('file-system');
var rl = require('readline-sync');

class ShareHolder{

    stock_list: Array<object>;
    stock_value:number;

    constructor(){
        this.stock_list = this.getCustomerStockList();
    }

    private readFile(){
        let file = fs.readFileSync('customerstockportfolio.json', 'utf8');
        return JSON.parse(file);
    }

    private getCustomerStockList(){
        let file = this.readFile();
        let result:Array<object> = [];
        for (var data in file['stock']){
            let share_details = file['stock'][data];
            result.push(share_details);
        }
        return result
    }

    valueOf(){
        let portfolio_value = 0;
        for (var i = 0; i < this.stock_list.length; i++){
            let amt = this.stock_list[i]['shareprice'] * this.stock_list[i]['numberofshares'];
            portfolio_value += amt;
        }
        console.log(`Total Share Holder Portfolio Value Is: ${portfolio_value}`);
    }

    // buyStock(stockname:string, numberofshares: number, shareprice:number){
    //     let stock_details = {
    //         "stockname": stockname,
    //         "numberofshares": numberofshares,
    //         "shareprice": shareprice
    //     }
    //     this.stock_list.push(stock_details)
    // }

    // sellStock(stockname:string){
    //     for (var i =0; i < this.stock_list.length; i++){
    //         if (stockname == this.stock_list[i]['stockname']){
    //             this.stock_list.splice(i, 1);
    //         }
    //     }
    // }
}

class CompanyListing{
    company_listings: Array<object>;

    constructor(){
        this.company_listings = this.getCompanyListings();
    }

    private readFile(){
        let file = fs.readFileSync('companylistings.json', 'utf8');
        return JSON.parse(file);
    }

    private getCompanyListings(){
        let file = this.readFile();
        let result:Array<object> = []
        for(var i in file['company']){
            let company_share = file['company'][i]
            result.push(company_share);
        }
        return result
    }

    addListing(company_name:string, numberofshares: number, shareprice:number){
        let company_details = {
            "name": company_name,
            "numberofshares": numberofshares,
            "shareprice": shareprice
        }
        this.company_listings.push(company_details)
    }
}

class StockAccount{

    owner: ShareHolder;
    company: CompanyListing;

    constructor(){
        this.owner = new ShareHolder();
        console.log(this.owner.stock_list)
        this.company = new CompanyListing();
        console.log(this.company.company_listings)
    }

    valueOf(){
        return this.owner.valueOf();
    }

    private checkForCompany(stockname :string):boolean{
        let data = this.company.company_listings;
        for(var i = 0; i < data.length; i++){
            if(stockname == data[i]['name']){
                return true
            }
        }
        return false
    }

    private getShareIndex(stockname){
        
    }

    // buyShares(){
    //     let stock_name = rl.question("Enter company name whose shares you would like to buy? :");
    //     let number_of_shares = parseInt(rl.question("Enter Number of Stocks"));
    //     if (this.checkForCompany(stock_name)){
    //         let company_list = this.company.company_listings
    //         for (var i = 0 ; i < company_list.length; i++){
    //             if (number_of_shares < this.company[i]['numberofshares']){

    //             }
    //         }
    //     }
    // }
}

let sa = new StockAccount()
// sa.buyShares();