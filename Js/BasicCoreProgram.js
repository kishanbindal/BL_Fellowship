"use strict";
exports.__esModule = true;
var readline = require("readline");
var process = require("process");
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
//------------------------------------------------------------------------------
function replaceString() {
    var sentence = "Hello <<UserName>>, How are you?";
    console.log("Sentence in which UserName has to be replaced :\n" + sentence);
    var name = rl.question('Please Enter your name: ', function (userInput) {
        console.log("Thank you for providing your name :" + userInput);
        var output = sentence.replace('<<UserName>>', userInput);
        console.log(output);
        rl.close();
        return userInput;
    });
}
var prompt = require('prompt');
function flipCoin() {
    prompt.start();
    prompt.get(['flip_count'], function (err, result) {
        console.log("Total Flip Count  : " + result.flip_count);
        var head_count = 0;
        var tail_count = 0;
        for (var i = 0; i < result.flip_count; i++) {
            var f = Math.random();
            if (f < 0.5) {
                head_count += 1;
            }
            else {
                tail_count += 1;
            }
        }
        console.log("Percentage Head Count : " + (head_count / result.flip_count) * 100);
        console.log("Percentage Tail Count : " + (tail_count / result.flip_count) * 100);
    });
}
function isLeapYear() {
    prompt.start();
    prompt.get(['year'], function (err, result) {
        try {
            if (result.year.length < 4) {
                throw Error("Year Must be a 4 digit number");
            }
            else {
                if ((result.year % 4 == 0) || (result.year % 400 == 0 && result.year % 100 != 0)) {
                    console.log(result.year + " is a leap year");
                    return true;
                }
                else {
                    console.log(result.year + " is not a leap year");
                    return false;
                }
            }
        }
        catch (err) {
            console.log(err);
        }
    });
}
// problem with powerOfTwo, Assigning Number
function powerOfTwo() {
    rl.question('Enter Number between 0 and 31 to get powers of 2: ', function (ans) {
        try {
            if (parseInt(ans) > 31 || parseInt(ans) < 1) {
                throw Error("Input Value cannot be greater than 31 nor less than 1");
            }
            else {
                for (var i = 1; i <= parseInt(ans); i++) {
                    console.log("2 to the power " + i + " = " + Math.pow(2, i));
                }
            }
        }
        catch (err) {
            console.log(err);
        }
        rl.close();
    });
}
;
function harmonicNumber() {
    rl.question('Enter Number for which you want to find Harmonic Number : \n', function (ans) {
        try {
            var x = parseInt(ans);
            if (x <= 0) {
                throw Error('Number has to be positive and greater than 0');
            }
            else {
                var result = 0;
                for (var i = 1; i <= x; i++) {
                    result = 1 / i;
                }
                console.log("Harmonic Number for " + x + " = " + result);
            }
        }
        catch (err) {
            console.log(err);
        }
        rl.close();
    });
}
function primeFactors() {
    rl.question('Enter Number >1 to find prime factors :\n', function (answer) {
        try {
            var num = parseInt(answer);
            if (num < 2) {
                throw Error('Number Has to be greater than equal to 2');
            }
            var i = 2;
            var result = [];
            while (num > 1) {
                if (num % i == 0) {
                    num = num / i;
                    result.push(i);
                }
                else {
                    i++;
                }
            }
            console.log(result);
        }
        catch (err) {
            console.log(err);
        }
        rl.close();
    });
}
primeFactors();
// function primeFactors(){
//     var num: number = async() => {
//         await var num = rl.question()
//     }
// }
// function primeFactors(){
//     new Promise((resolve,reject)=> {
//         var num = rl.question("Enter Number to find prime factors :\n", function(answer){
//             var x:number  = parseInt(answer)
//             resolve(x)
//             rl.close();
//         })
//     }).then(x=> {
//         console.log(`Value of X : ${x}`);
//         // console.log(typeof(x))
//         var i = 2;
//         var result: number[] = [];
//         while (x > 2){
//         //     if (x % i == 0){
//         //         x = x / i;
//         //         result.push(i)
//         //     }else{
//         //         i++;
//         //     }
//         }
//         console.log(result)
//         return result;
//     })
// }
// var x = primeFactors()
// console.log(x);
// rl.on('close', () => {
//     console.log('Thank you for your input');
// });
