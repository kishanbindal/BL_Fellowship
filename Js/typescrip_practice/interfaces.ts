// Interface is a Syntactical Contract that an entity should conform to
// in other words, an interface defines the syntax an entity must adhere to
// Functions cannot be defined in an interface.
// signature of the method is created for classes to implement them.

interface Person{
    firstName: string;
    lastName: string;
    getFullName(): string;
}

class Foo implements Person{
    firstName: string;
    lastName: string;
    getFullName(): string {
        return `${this.firstName} ${this.lastName}`
    }
}

let a:Person = new Foo();

// doesnt enforce above entirely. you can create an object that hass all th eproperties of the interface
// Even if the class does not implement the Interface.

let someObj = {
    firstName: "Test",
    lastName: "Test",
    getFullName: () => "Test",
    foo: 10,
};

a = someObj; // someObj has same structure as Person. This structure is referred to as Duck Typing.
// This will work fine until the properties strictly match.
// a.foo Error because foo is not in the interface.
