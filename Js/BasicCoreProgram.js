"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
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
// function primeFactors(){
//     rl.question('Enter Number >1 to find prime factors :\n', function(answer){
//         try{
//             var num = parseInt(answer)
//             if (num < 2){
//                 throw Error('Number Has to be greater than equal to 2');
//             }
//             var i = 2;
//             var result: number[] = []
//             while(num > 1){
//                 if(num%i ==0){
//                     num = num / i;
//                     result.push(i);
//                 }else{
//                     i++;
//                 }
//             }
//             console.log(result);
//         }catch(err){ 
//             console.log(err);
//         }
//         rl.close();
//     })
// }
// primeFactors()
// function primeFactors(){
//     var num: number = async() => {
//         await var num = rl.question()
//     }
// }
// function primeFactors(){
//     new Promise((resolve,reject)=> {
//         var num = rl.question("Enter Number to find prime factors :\n", function(answer){
//             var x:number  = parseInt(answer);
//             rl.close(); 
//             return x;   
//         })
//         resolve(console.log(typeof(num));
//     })
// }
function primeFactors() {
    var num = rl.question("Enter Number to find prime factors :\n", function (answer) {
        var x = parseInt(answer);
        rl.close();
        return x;
    });
}
(function () { return __awaiter(void 0, void 0, void 0, function () {
    var _a, _b;
    return __generator(this, function (_c) {
        switch (_c.label) {
            case 0:
                _b = (_a = console).log;
                return [4 /*yield*/, (primeFactors())];
            case 1:
                _b.apply(_a, [_c.sent()]);
                return [2 /*return*/];
        }
    });
}); });
// primeFactors();
// console.log('Kishan');
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
//
