import { type } from "os";
import { stat } from "fs";
import { isString, isNumber } from "util";
import { parse } from "querystring";

var rl = require('readline-sync');
var rf = require('fs');

function getData(obj:object): Person{
    var first_name:string = obj['first_name'];
    var last_name:string = obj['last_name'];
    var address:string = obj['address'];
    var city:string = obj['city'];
    var state:string = obj['state'];
    var zip:number = obj['zip'];
    var number:number = obj['phone_number'];
    var person = new Person(first_name, last_name, address, city, state, zip,number)
    return person;
}

// function getUserEditData(){
//     var address:string = rl.question("Enter Address :\n");
//     var city:string = rl.question("Enter City :\n");
//     var state:string = rl.question("Enter State :\n");
//     var zip:number = parseInt(rl.question("Enter ZIP Code :\n"));
//     var phone_number:number = parseInt(rl.question("Enter contact number :\n"));
// }

// function getUserInputData(){
//     var first_name:string = rl.question("Enter First Name :\n");
//     var last_name:string = rl.question("Enter Last Name:\n");
//     getUserEditData();
// }

class Person{

    first_name: string;
    last_name: string;
    address: string;
    city: string;
    state: string;
    zip: number;
    phone_number: number;

    constructor(first_name:string, last_name:string, address:string, city:string, state:string, zip:number, phone_number:number){
        this.first_name = first_name;
        this.last_name = last_name;
        this.address = address;
        this.city = city;
        this.state = state;
        this.zip = zip;
        this.phone_number = phone_number;
    }
}

class AddressBook {

    list_of_people: object[];

    constructor(){
        this.list_of_people = this.getPeople();
    }

    private getPeople(): object[]{
        var fs = require('file-system');
        var file = fs.readFileSync('addressbook.json', 'utf8');
        file = JSON.parse(file);
        let people:object[] =[]
        for (var person in file){
            people.push(getData(file[person]));
        }
        return people
    }

    displayPeople() {
        this.list_of_people.forEach(people => {
            console.log(`Full Name : ${people['first_name']} ${people['last_name']}`);
            console.log(`Address : ${people['address']}\nCity: ${people['city']}\nState: ${people['state']}`);
            console.log(`ZIP Code: ${people['zip']}\nPhone Number: ${people['phone_number']}\n`);
        });
    }

    addPeople(){
        try{
            var first_name:string = rl.question("Enter First Name :\n");
            var last_name:string = rl.question("Enter Last Name:\n");
            var address:string = rl.question("Enter Address :\n");
            var city:string = rl.question("Enter City :\n");
            var state:string = rl.question("Enter State :\n");
            var zip:number = parseInt(rl.question("Enter ZIP Code :\n"));
            var phone_number:number = parseInt(rl.question("Enter contact number :\n"));
            if (isString(first_name) && isString(last_name) && isString(address) && isString(city) && isString(state)
                && isNumber(zip) && isNumber(phone_number)){
                let person = new Person(first_name, last_name, address, city, state, zip, phone_number)
                this.list_of_people.push(person);
                console.log(`Successfully added ${person.first_name} ${last_name} to AddressBook\n`);
            }else{
                throw Error("Input Validation failed due to incorrect input data types.");
            }  
        }catch(err){
            console.log(err);
        }   
    }
    // addPeople(first_name:string, last_name:string, address:string, city:string, state:string, zip:number, phone_number:number){
    //     let person = new Person(first_name, last_name, address, city, state, zip, phone_number);
    //     this.list_of_people.push(person);
    // }

    editUserData(){
        let fname:string = rl.question("Enter First Name of Customer whose entry you would like to edit :\n");
        let lname:string = rl.question("Enter Last Name of Customer whose entry you would like to edit :\n");
        this.list_of_people.forEach(person => {
            if(fname == person['first_name'] && lname == person['last_name']){
                var address:string = rl.question("Enter Address :\n");
                var city:string = rl.question("Enter City :\n");
                var state:string = rl.question("Enter State :\n");
                var zip:number = parseInt(rl.question("Enter ZIP Code :\n"));
                var phone_number:number = parseInt(rl.question("Enter contact number :\n"));
                person['address'] = address; person['city'] = city; person['state'] = state; person['zip'] = zip;
                person['phone_number'] = phone_number;
            }else{
                console.log("Could Not Find Entry");
            }
        });
        
    }

    deleteUser(){
        let fname = rl.question("Enter First Name of Customer whose entry you would like to edit :\n");
        let lname = rl.question("Enter Last Name of Customer whose entry you would like to edit :\n");
        for (var i = 0; i < this.list_of_people.length; i++){
            if (fname == this.list_of_people[i]['first_name'] && lname == this.list_of_people[i]['last_name']){
                this.list_of_people.splice(i,1);
            }
        }
    }

    save(){
        let data = JSON.stringify(this.list_of_people);
        rf.writeFileSync('modifiedAddressBook.json', data);
    }

}

function main(){
    console.log('--------ADDRESS BOOK-----------------');
    // console.log('\t   OPTIONS');
    // console.log('1. View All Entries\n2. Add Person to AddressBook\n3. Edit Details\n4. Delete Entry\n5. Save\n6. Close');
    var ab = new AddressBook();
    while (true){
        console.log('\t   OPTIONS');
        console.log('1. View All Entries\n2. Add Person to AddressBook\n3. Edit Details\n4. Delete Entry\n5. Save\n6. Close\n');    
        var userInput = parseInt(rl.question("Please choose your option (1-6)\n"));
        if (userInput== 1){
            ab.displayPeople();
        }else if (userInput == 2){
            ab.addPeople();
        }else if (userInput == 3){
            ab.editUserData();
        }else if(userInput ==4){
            ab.deleteUser();
        }else if(userInput == 5){
            ab.save();
        }else if(userInput == 6){
            break;
        }else{
            console.log("Please Enter Valid Input\n");
        }
    }
    
}

main();

// var ab = new AddressBook();
// ab.displayPeople();
// ab.deleteUser();
// ab.displayPeople();
// ab.save();

// var person  = new Person('Kishan', 'Bindal', 'blr' ,'Bangalore', 'Karnataka', 560037, 9185421365);
// console.log(person.first_name);
