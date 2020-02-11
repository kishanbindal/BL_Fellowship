//---------------------------BASIC TYPE DECLARATION AND DATA TYPES--------------------------------
var a: number; // type declaration in typescript

var b: boolean; // post-fix declaration. Type is being declared after the variable name 

var c: string;

// Arrays
var d: number[]; 

var e: Array<number>;

//Tuples (Allow you to express and array with fixed number of elements whose data types are known, but need not be the same)
let tup: [string, number];

//Languages like Java have prefix: example ---> int a = 10 (or) String a = 'Kishan';


a = 10;
b = true; 
c = 'Kishan'; 
d = [1, 2, 3];
e = [4, 5, 6];
tup = ['Kishan', 5];

let li: [number, boolean, string, Array<number>, Array<number>, [string, number]]
li = [a, b, c, d, e, tup];
for(var i = 0; i < li.length; i++){
    console.log(li[i]);
}
//--------------------------------------------Functions-------------------------------------------
function add(a:number , b:number){
    return a+b;
}

// var sum = add(5,2)
// console.log(sum); 

// Function With Variable Arguments(optional paramenters)
// '?' after variable means that it is optional


let myAdd: (baseValue: number, increment: number) => number =
    function(x: number, y: number): number { return x + y; };

// Optional Arguments
function addOptional(a:number, b:number, c?: number){
    if (c){
        return a+b+c;
    }
    else{
        return a+b;
    }
}
// Can also be written like with default Arguments:

function buildName(firstName: string, lastName = ''){
    return firstName + " " + lastName
}

var sum = addOptional(5,5)
console.log(`Sum without optional variable : ${sum}`)
console.log(`\nName : ${buildName('Kishan')}`)

// Rest Parameters
function buildRestName(firstName:string, lastName:string, otherNames:string[]){
    return firstName+" " + lastName + " " + otherNames.join(" ");
}

console.log(`Hello ${buildRestName('Adolf', 'Blaine', ['Charles', 'David', 'Earle'])}`)