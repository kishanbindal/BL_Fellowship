var fs = require('file-system');
var rl = require('readline-sync');

class Inventory{

    items:object[];

    constructor(){
        this.items = this.getInventory();
    }

    getInventory(){
        let file = fs.readFileSync('inventory.json', 'utf8');
        file = JSON.parse(file);
        var inventory = []
        for (var item in file.inventory){
            console.log(file.inventory[item].item);
        }
        return []
    }
}
let im = new Inventory();

// let file = fs.readFileSync('inventory.json', 'utf8')
// // console.log(file);

// file = JSON.parse(file);
// console.log(file.inventory[0]);