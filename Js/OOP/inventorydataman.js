var fs = require('file-system');
var rl = require('readline-sync');
var Inventory = /** @class */ (function () {
    function Inventory() {
        this.items = this.getInventory();
    }
    Inventory.prototype.getInventory = function () {
        var file = fs.readFileSync('inventory.json', 'utf8');
        file = JSON.parse(file);
        var inventory = [];
        for (var item in file.inventory) {
            console.log(file.inventory[item].item);
        }
        return [];
    };
    return Inventory;
}());
var im = new Inventory();
// let file = fs.readFileSync('inventory.json', 'utf8')
// // console.log(file);
// file = JSON.parse(file);
// console.log(file.inventory[0]);
