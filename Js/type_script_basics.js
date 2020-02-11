//---------------------------BASIC TYPE DECLARATION AND DATA TYPES--------------------------------
var a; // type declaration in typescript
var b; // post-fix declaration. Type is being declared after the variable name 
var c;
// Arrays
var d;
var e;
//Tuples (Allow you to express and array with fixed number of elements whose data types are known, but need not be the same)
var tup;
//Languages like Java have prefix: example ---> int a = 10 (or) String a = 'Kishan';
a = 10;
b = true;
c = 'Kishan';
d = [1, 2, 3];
e = [4, 5, 6];
tup = ['Kishan', 5];
var li;
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
var myAdd = function (x, y) { return x + y; };
function addOptional(a, b, c) {
    if (c) {
        return a + b + c;
    }
    else {
        return a + b;
    }
}
// Can also be written like :
function buildName(firstName, lastName) {
    if (lastName === void 0) { lastName = ''; }
    return firstName + " " + lastName;
}
var sum = addOptional(5, 5);
console.log("Sum without optional variable : " + sum);
console.log("\nName : " + buildName('Kishan'));
// Rest Parameters
function buildRestName(firstName, lastName, otherNames) {
    return firstName + " " + lastName + " " + otherNames.join(" ");
}
console.log("Hello " + buildRestName('Adolf', 'Blaine', ['Charles', 'David', 'Earle']));
