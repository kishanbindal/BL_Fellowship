// ---------------------------------BASIC CORE PROGRAMS--------------------------------------------
function replaceString(){
    sentence = "Hello <<username>>, How are you?";
    alert(`Sentence for name to be Added in is : \n ${sentence}`);
    name = prompt("Please Enter Your name : ");
    sentence = sentence.replace('<<username>>', name);
    alert(sentence);
    console.log(sentence);
}

function flipCoin(){
    flip_count = prompt("How many times would you like to flip coin?");
    head_count = 0;
    tail_count = 0;
    for (var i = 0; i < flip_count;i++){
        face_value = Math.random();
        if (face_value <= 0.5){
            head_count += 1;
        }
        else{
            tail_count += 1;
        }
    }
    // alert(`Percentage Heads = ${(head_count/flip_count)*100}`);
    // alert(`Percentage Tails = ${(tail_count/flip_count)*100}`);
    console.log(`Percentage Heads = ${(head_count/flip_count)*100}`);
    console.log(`Percentage Tails = ${(tail_count/flip_count)*100}`);
}

function isLeapYear(){
    year = prompt("Checking For Leap Year\nPlease Enter Year that you would Like To Check:");
    if(year%4 ==0 || (year%400 == 0 && year%100 != 0)){
        console.log(`${year} is a leap year`);
        return true;
    }else{
        console.log(`${year} is not a Leap Year`);
        return false;
    }
}

function powerOf2(){
    try{
        n = prompt("Enter integer value of number < 31")
        if(n>30 || n < 0){
            throw Error("Value Cannot be greater than 30 nor less than 0");
        }else{
            for(var i = 0; i <=n; i++){
                console.log(`2 x ${i} = ${2**i}`)
            }
        }
    }catch(err){
        console.log(err);
    } 
}

function harmonicNumber(){
    try{
        n = prompt('Please Enter Number > 0 for which you want to calculate Harmonic Number :');
        if (n<1){
            throw Error("Value Has to be greater than 0");
        }else{
            result = 0;
            for(var i = 1; i <= n; i++){
                result = result + (1/i);
            }
            console.log(`Harmonic Number : ${result}`)
        }
    }catch(err){
        console.log(err);
    }
}
//-----------------------------------FUNCTIONAL PROGRAMS--------------------------------------
function sumOfThree(){
    inputs = []
    for (var i =1; i<=3; i++){
        x = prompt(`Enter ${i}th Number`)
        inputs.push(x)
    }
    console.log(`Inputs are ${inputs}`)
    sum = 0
    for(var i =0; i < inputs.length; i++){
        sum = sum + parseInt(inputs[i]);
    }
    console.log(sum);
    if (sum == 0){
        return true;
    }
    return false
}

function distance(){
    x = prompt('Enter X co-ordinate :');
    y = prompt('Enter Y co-ordinate :');
    distance = ((x*x)+(y*y))**0.5;
    console.log(distance);
}

function windChill(){
    try{
        t = prompt('Enter Temperature in Fahrenheit (t <= 50)');
        v = prompt("Enter Wind Speed in mph (3 < value < 120)");
        if(t > 50 || v < 3 || v > 120 ){
            throw Error('Value Of temperature cannot exceed 50 and v has to be in between 3 and 120')
        }else{
            windchill = 35.74 + 0.6215*t + (0.4275*t - 35.75)*(v**0.16);
            console.log(`windchill : ${windchill}`)
            return windchill
        }
    }catch(err){
        console.log(err);
    }
}
//-----------------------------------LOGICAL PROGRAMS---------------------------------------------






// distance()
// console.log(windChill())

// function Factors(){
//     try{
//         n = prompt('Enter Postive Number above 1')
//         if(n< 2){
//             throw Error("Number cannot be less than 2 for computation");
//         }else{
//             console.log(`Input number is : ${n}`);
//             result = [];
//             var i = 2;
//             while (n > 2){
//                 if(n%i == 0){
//                     n  = n/i;
//                     result.push(i)
//                 }else{
//                     i++;
//                 }
//                 }
//             console.log(result);
//             }
//         }catch(err){
//             console.log(err);
//         }
//     }

// replaceString()
// flipCoin()
// isLeapYear()                                                                                                                                                                                                                                                                                                                                                                             
// powerOf2()
// harmonicNumber()
// Factors()