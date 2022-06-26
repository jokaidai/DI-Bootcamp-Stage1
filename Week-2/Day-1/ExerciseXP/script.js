//VAR

//EX1
let fav_food = "pizza";
let fav_meal = "lunch";
//EX1

//EX2.a
let my_watched_series = ["Obi-Wan Kenobi", " Game Of Thrones", " Suits"];
let my_watched_series_length = my_watched_series.length;
let my_watched_series_sentence = my_watched_series.toString();
//EX2.a

//EX2.b
let deleted_index = my_watched_series.indexOf(" Suits"); //will be used in the futur as a function with the input from the user
//EX2.b

//EX3
let temperature_cel = 26; //will be used in the futur as a function with the input from the user
let tempereture_far = temperature_cel / 5 * 9 + 32
//EX3

//VAR

console.log('=====EX1====='+'');
console.log(`I eat ${fav_food} at every ${fav_meal}`); //EX1

console.log('=====EX2.a====='+'');
console.log(`I watched ${my_watched_series_length} series : ${my_watched_series_sentence}`); //EX2.a

console.log('=====EX2.b====='+'');
//EX2.b
my_watched_series[deleted_index] = "Friends";
//console.log(my_watched_series); // if you want to watch progression 
my_watched_series.push(" Breaking Bad");
//console.log(my_watched_series); // if you want to watch progression 
my_watched_series.unshift(" One Piece");
//console.log(my_watched_series); // if you want to watch progression 
my_watched_series.splice(1, 1);
console.log(my_watched_series[1] [13]); // did it with game of thrones letter n because i dont have money heist in my array
console.log(my_watched_series);
//EX2.b 

console.log('=====EX3====='+'');
//EX3
console.log(`${temperature_cel}°C is ${tempereture_far.toFixed(2)}°F`);
//EX3 

console.log('=====EX4====='+'');

//EX4
let c;
let a = 34;
let b = 21;

    console.log(a+b); //first expression
    // Prediction: 55
    // Actual: 55

    a = 2;

    console.log(a+b); //second expression
    // Prediction: 23
    // Actual: 23

    console.log(c);
    //Prediction: Undefined
    //Actual: Undefined

    console.log(3 + 4 + '5');
    //Prediction: 75
    //Actual: 75
    //Ex4

    console.log('=====EX5====='+'');

    //EX5
    console.log(typeof(15));
// Prediction:Number
// Actual: Number

console.log(typeof(5.5));
// Prediction:Number
// Actual: Number

console.log(typeof(NaN));
// Prediction:Number (it just mean that tthe num we check is outside the scope but its still a number)
// Actual: Number

console.log(typeof("hello"));
// Prediction: string
// Actual: string

console.log(typeof(true));
// Prediction: boolean
// Actual: boolean

console.log(typeof(1 != 2));
// Prediction: boolean (1 != 2 return true, true is boolean)
// Actual: boolean

console.log("hamburger" + "s");
// Prediction: hamburgers
// Actual:hamburgers

console.log("hamburgers" - "s");
// Prediction: hamburger
// Actual: NaN ??

console.log("1" + "3");
// Prediction: 13
// Actual: 13

console.log("1" - "3");
// Prediction: NaN
// Actual: -2 (WTF ??? those are strings so why ??)

console.log("johnny" + 5);
// Prediction: jhonny5
// Actual: jhonny5

console.log("johnny" - 5);
// Prediction: NaN 
// Actual: NaN 

console.log(99 * "hello");
// Prediction:99 times hello !?
// Actual:NaN

console.log(1 != 1);
// Prediction: false
// Actual:false

console.log(1 == "1");
// Prediction: false the number 1 and the string 1 are not considered equals
// Actual: true ...

console.log(1 === "1");
// Prediction: false (if it was 2 strings then yes but here the inside value is equal but not the type)
// Actual: false
//EX5


console.log('=====EX6====='+'');
//EX6
console.log(5 + "34");
// Prediction: 534
// Actual: 534

console.log(5 - "4");
// Prediction: 1 (dont really know why but it happened like that in EX5!!)
// Actual: 1

console.log(10 % 5);
// Prediction: 0.5
// Actual: 0 

console.log(5 % 10);
// Prediction: 0.5
// Actual: 5

console.log("Java" + "Script");
// Prediction: JavaScript
// Actual: JavaScript

console.log(" " + " ");
// Prediction:   (empty space)
// Actual:   (empty space)

console.log(" " + 0);
// Prediction: 0
// Actual: 0

console.log(true + true);
// Prediction: false (true + true = 1 + 1 = 2, 2 is false ...)
// Actual: 2

console.log(true + false);
// Prediction: true (true + false = 1 + 0 = 1, 1 is true)
// Actual: 1

console.log(false + true);
// Prediction: true (false + true = 0 + 1 = 1, 1 is true)
// Actual: 1

console.log(false - true);
// Prediction: null (false - true = 0 - 1 = -1, boolean do not include negative numbers) 
// Actual: -1 

console.log(!true);
// Prediction: false (! = not)
// Actual: false

console.log(3 - 4);
// Prediction:-1
// Actual:

console.log("Bob" - "bill");
// Prediction:NaN
// Actual:
//EX6