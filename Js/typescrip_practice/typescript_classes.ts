class Person {
    firstName: string;
    lastName: string;

    // constructor(){
    //     this.firstName = ' ';
    //     this.lastName = ' ';
    // }

    constructor(firstName: string, lastName: string){
        this.firstName = firstName;
        this.lastName = lastName;
    }

    getFullName(): string{
        return `${this.firstName} ${this.lastName}`
    }

    greet(): void{
        console.log('Hey There!');
    }
}

class Programmer extends Person {
    
    greet(): void{
        console.log('Hello World!')
    }

    greetPerson(){
        super.greet();
    }
}

var a: Programmer = new Programmer('Kishan', 'Bindal');
// var a: Person = new Programmer('Kishan', 'Bindal') Polymorphism, member variables and methods of :type are the only ones that can be used.

console.log(a.getFullName());
a.greet();
a.greetPerson();

//---------------Basic Implementation---------------
// var a:Person = new Person();
// a.firstName = 'Kishan'; a.lastName = 'Bindal'

// var a = new Person('Kishan', 'Bindal');
// console.log(a.getFullName());
