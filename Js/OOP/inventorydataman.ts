var fs = require('file-system');
var rl = require('readline-sync');

class Inventory{

    item:string;
    ppk: number;
    weight:number;

    constructor(item:string, weight:number, ppk:number){
        this.item = item;
        this.weight = weight;
        this.ppk = ppk;
    }
}

class InventoryManager{

    items:object[];

    constructor(){
        this.items = this.getInventory();
    }

    // Used to get data from JSON File and this.items
    private getInventoryData(data): [string, number, number]    
    {
        var item_name = data['item'];
        var item_weight = data['weight'];
        var item_ppk = data['ppk'];
        return [item_name, item_weight, item_ppk];
    }

    private getInventory()
    // Used to add Inventroy objects in this.items.
    {
        let file = fs.readFileSync('inventory.json', 'utf8');
        file = JSON.parse(file);
        var inventory = []
        for (var item in file.inventory){
            let items = file.inventory[item];
            let data: [string, number, number] = this.getInventoryData(items);
            let inventory_obj = new Inventory(data[0], data[1], data[2]);
            inventory.push(inventory_obj);
        }
        return inventory;
    }

    displayInventory()
    // Display all items in the inventory and their cost and total Value of Inventrory
    {
        var i = 1;
        console.log("\t\tInventory Details")
        let sum = 0;
        this.items.forEach(item => {
            var data = this.getInventoryData(item);
            console.log('----------------------------------------------------------');
            console.log(`     Item ${i}\nItem Name: ${data[0]}\nItem Weight: ${data[1]}\nPrice Per Kg: ${data[2]}`);
            console.log(`Value of ${data[0]} in inventory is : ${data[1]*data[2]}\n`);
            sum += data[1]*data[2];
            i +=1;
        });
        console.log(`Total Inventory Value: ${sum}`);
    }

    addToInventory()
    // Adds Item to Inventory
    {
        var item_name: string = rl.question('Enter Name of item you would like to add to Inventroy:\n');
        var item_weight: number = parseInt(rl.question('Enter weight of item you would like to add to Inventroy:\n'));
        var item_ppk:number = parseInt(rl.question('Enter Price/Kg of item you would like to add to Inventroy:\n'));
        let inventory_obj = new Inventory(item_name, item_weight, item_ppk);
        this.items.push(inventory_obj);
    }

    editInventory()
    //Edits the item in inventory provided it exists in the Inventory
    {
        let item_name:string = rl.question('Enter Name of Item you would like to Edit? \n')
        for (var i =0; i < this.items.length; i++){
            if (this.items[i]['item'].toLowerCase() == item_name.toLowerCase()){
                while(true){
                    console.log(`     EDIT SUBMENU for ${this.items[i]['item']}\n--------------------------------`)
                    console.log('1. Edit Weight\n2. Edit Price Per Kg\n3. Exit Submenu')
                    let choice:number = parseInt(rl.question('Enter Choice (1-3)'));
                    if (choice == 1){
                        let new_weight = rl.question("Enter Updated Weight :\n");
                        this.items[i]['weight'] = new_weight;
                    }else if(choice == 2){
                        let new_ppk = parseInt(rl.question("Updated Price per Kig?\n"));
                        this.items[i]['ppk'] = new_ppk;
                    }else if(choice == 3){
                        break;
                    }else{
                        console.log("Invalid Input. Input must be numbers between 1 and 3");
                    }
                }
            }
        }
    }

    removeFromInventory()
    // Removes an item from Inventroy provided the item exists in the inventory.
    {
        let item_name:string = rl.question('\nEnter item you would like to remove from Inventory: \n');
        for (var i =0; i<this.items.length; i++){
            if (this.items[i]['item'].toLowerCase() == item_name.toLowerCase()){
                this.items.splice(i,1);
            }
        }
    }

    save()
    //Saves the data into a file called updatedInventory.json. (can be changed to original file for overwriting)
    {
        let data = JSON.stringify(this.items);
        fs.writeFileSync('updatedInventory.json', data);
    }
}

function main(){
    var im = new InventoryManager();
    while(true){
        console.log('\t OPTIONS\n-----------------------------------------')
        console.log('1. Display Items in inventory\n2. Add Item to Inventory\n3. Edit item in Inventory');
        console.log('4. Delete Item from Inventory\n5.Save\n6. Exit')
        let choice = parseInt((rl.question('Enter Choice between 1 to 6:\n')));
        if (choice == 1){
            im.displayInventory();
        }else if (choice == 2){
            im.addToInventory();
        }else if (choice == 3){
            im.editInventory();
        }else if(choice == 4){
            im.removeFromInventory();
        }else if(choice == 5){
            im.save();
        }else if(choice == 6){
            break;
        }else{
            console.log("Please Enter Valid Data. Numbers between 1 and 6 Only.")
        }
    }
}

main();