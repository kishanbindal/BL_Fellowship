var fs = require('file-system');
var rl = require('readline-sync');
var Inventory = /** @class */ (function () {
    function Inventory(item, weight, ppk) {
        this.item = item;
        this.weight = weight;
        this.ppk = ppk;
    }
    return Inventory;
}());
var InventoryManager = /** @class */ (function () {
    function InventoryManager() {
        this.items = this.getInventory();
    }
    InventoryManager.prototype.getInventoryData = function (data) {
        var item_name = data['item'];
        var item_weight = data['weight'];
        var item_ppk = data['ppk'];
        return [item_name, item_weight, item_ppk];
    };
    InventoryManager.prototype.getInventory = function () {
        var file = fs.readFileSync('inventory.json', 'utf8');
        file = JSON.parse(file);
        var inventory = [];
        for (var item in file.inventory) {
            var items = file.inventory[item];
            var data = this.getInventoryData(items);
            var inventory_obj = new Inventory(data[0], data[1], data[2]);
            inventory.push(inventory_obj);
        }
        return inventory;
    };
    InventoryManager.prototype.displayInventory = function () {
        var _this = this;
        var i = 1;
        console.log("\t\tInventory Details");
        var sum = 0;
        this.items.forEach(function (item) {
            var data = _this.getInventoryData(item);
            console.log('----------------------------------------------------------');
            console.log("     Item " + i + "\nItem Name: " + data[0] + "\nItem Weight: " + data[1] + "\nPrice Per Kg: " + data[2]);
            console.log("Value of " + data[0] + " in inventory is : " + data[1] * data[2] + "\n");
            sum += data[1] * data[2];
            i += 1;
        });
        console.log("Total Inventory Value: " + sum);
    };
    InventoryManager.prototype.addToInventory = function () {
        var item_name = rl.question('Enter Name of item you would like to add to Inventroy:\n');
        var item_weight = parseInt(rl.question('Enter weight of item you would like to add to Inventroy:\n'));
        var item_ppk = parseInt(rl.question('Enter Price/Kg of item you would like to add to Inventroy:\n'));
        var inventory_obj = new Inventory(item_name, item_weight, item_ppk);
        this.items.push(inventory_obj);
    };
    InventoryManager.prototype.editInventory = function () {
        var item_name = rl.question('Enter Name of Item you would like to Edit? \n');
        for (var i = 0; i < this.items.length; i++) {
            if (this.items[i]['item'].toLowerCase() == item_name.toLowerCase()) {
                while (true) {
                    console.log("     EDIT SUBMENU for " + this.items[i]['item'] + "\n--------------------------------");
                    console.log('1. Edit Weight\n2. Edit Price Per Kg\n3. Exit Submenu');
                    var choice = parseInt(rl.question('Enter Choice (1-3)'));
                    if (choice == 1) {
                        var new_weight = rl.question("Enter Updated Weight :\n");
                        this.items[i]['weight'] = new_weight;
                    }
                    else if (choice == 2) {
                        var new_ppk = parseInt(rl.question("Updated Price per Kig?\n"));
                        this.items[i]['ppk'] = new_ppk;
                    }
                    else if (choice == 3) {
                        break;
                    }
                    else {
                        console.log("Invalid Input. Input must be numbers between 1 and 3");
                    }
                }
            }
        }
    };
    InventoryManager.prototype.removeFromInventory = function () {
        var item_name = rl.question('\nEnter item you would like to remove from Inventory: \n');
        for (var i = 0; i < this.items.length; i++) {
            if (this.items[i]['item'].toLowerCase() == item_name.toLowerCase()) {
                this.items.splice(i, 1);
            }
        }
    };
    InventoryManager.prototype.save = function () {
        var data = JSON.stringify(this.items);
        fs.writeFileSync('updatedInventory.json', data);
    };
    return InventoryManager;
}());
function main() {
    var im = new InventoryManager();
    while (true) {
        console.log('\t OPTIONS\n-----------------------------------------');
        console.log('1. Display Items in inventory\n2. Add Item to Inventory\n3. Edit item in Inventory');
        console.log('4. Delete Item from Inventory\n5.Save\n6. Exit');
        var choice = parseInt((rl.question('Enter Choice between 1 to 6:\n')));
        if (choice == 1) {
            im.displayInventory();
        }
        else if (choice == 2) {
            im.addToInventory();
        }
        else if (choice == 3) {
            im.editInventory();
        }
        else if (choice == 4) {
            im.removeFromInventory();
        }
        else if (choice == 5) {
            im.save();
        }
        else if (choice == 6) {
            break;
        }
        else {
            console.log("Please Enter Valid Data. Numbers between 1 and 6 Only.");
        }
    }
}
main();
