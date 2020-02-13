//---------------------------BASIC TYPE DECLARATION AND DATA TYPES--------------------------------
var a; // type declaration in typescript
var b; // post-fix declaration. Type is being declared after the variable name 
var c;
// Arrays
var d;
var e;
//Tuples (Allow you to express and array with fixed number of elements whose data types are known, but need not be the same)
let tup;
//Languages like Java have prefix: example ---> int a = 10 (or) String a = 'Kishan';
a = 10;
b = true;
c = 'Kishan';
d = [1, 2, 3];
e = [4, 5, 6];
tup = ['Kishan', 5];
let li;
li = [a, b, c, d, e, tup];
for (var i = 0; i < li.length; i++) {
    console.log(li[i]);
}
//--------------------------------------------Functions-------------------------------------------
function add(a, b) {
    return a + b;
}
// var sum = add(5,2)
// console.log(sum); 
// Function With Variable Arguments(optional paramenters)
// '?' after variable means that it is optional
let myAdd = function (x, y) { return x + y; };
// Optional Arguments
function addOptional(a, b, c) {
    if (c) {
        return a + b + c;
    }
    else {
        return a + b;
    }
}
// Can also be written like with default Arguments:
function buildName(firstName, lastName = '') {
    return firstName + " " + lastName;
}
var sum = addOptional(5, 5);
console.log(`Sum without optional variable : ${sum}`);
console.log(`\nName : ${buildName('Kishan')}`);
// Rest Parameters
function buildRestName(firstName, lastName, otherNames) {
    return firstName + " " + lastName + " " + otherNames.join(" ");
}
console.log(`Hello ${buildRestName('Adolf', 'Blaine', ['Charles', 'David', 'Earle'])}`);
// -----------------------------------------------IMPLICIT ASSIGNMENT--------------------------------------------
// Assingment and declartion need to be on the same line for implicit typing, eg:- 
var ab; // Implicit typing gives the variable ab type: any
ab = true;
ab = 10;
var xyz = 10;
// xyz = "kishan" Throws Error, since it has binded xyz(xyz: number) due to assignment. var xyz will only take in numbers
// Union allows for binding between two values (similar to 'or' gate)
// var xyz : number | string -------> This is called Union. will give error when any datatype other than these two are passed.
// Can have as many Unions, but it's better to keep it on the lower side. 
//# sourceMappingURL=type_script_basics.js.map