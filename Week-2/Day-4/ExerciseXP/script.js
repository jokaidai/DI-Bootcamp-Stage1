//EX1
/*
Instructions

Part I : function with no parameters

1.Create a function called infoAboutMe() that takes no parameter.
2.The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
3.Call the function.


Part II : function with three parameters

1.Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.

2.The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)

3.Call the function twice with the following arguments:
	infoAboutPerson("David", 45, "blue")
	1infoAboutPerson("Josh", 12, "yellow")
	*/

//PART 1
function infoAboutMe(){
	console.log("My name is Elie and i am a serious nerd !!!, i love video game and manga!! I want to become a game designer someday :)");
}

infoAboutMe();

//PART 2
function infoAboutPerson(personName, personAge, personFavoriteColor){
	console.log(`You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`)
}

infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");
//EX1

//EX2
/*
Instructions

John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

1.Create a function named calculateTip() that takes no parameter.

2.Inside the function, ask John for the amount of the bill.

3.Here are the rules
	If the bill is less than $50, tip 20%.
	If the bill is between $50 and $200, tip 15%.
	If the bill is more than $200, tip 10%.

4.Console.log the tip amount and the final bill (bill + tip).

5.Call the calculateTip() function.
*/

// function calculateTip(){

// 	let bill = prompt("What is the amount of your bill ?");
// 	bill = Number(bill);
// 	let tip;

// 	switch(true) {

// 		case bill < 50:
// 		tip = "20%"
// 		return `You need to tip ${tip}.`;

// 		case bill >= 50 && bill <= 200 :
// 		tip = "15%"
// 		return `You need to tip ${tip}.`;

// 		case bill > 200:
// 		tip = "10%"
// 		return `You need to tip ${tip}.`;
// 	}
// } 
// console.log(calculateTip());
//EX2

//EX3
/*
Instructions

1.Create a function call isDivisible() that takes no parameter.

2.In the function, loop through numbers 0 to 500.

3.Console.log all the numbers divisible by 23.

4.At the end, console.log the sum of all numbers that are divisible by 23.

Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
391 414 437 460 483
Sum : 5313


5.Bonus: Add a parameter divisor to the function.

isDivisible(divisor)

Example:
isDivisible(3) : Console.log all the numbers divisible by 3, and their sum
isDivisible(45) : Console.log all the numbers divisible by 45, and their sum

*/

function isDivisible(divisor){

	let sum_div = 0;
	for(let i = 0; i < 500; i++){
		if (i % divisor == 0){
			sum_div += i;
			console.log(i);
		}
	}
	console.log(`Sum : ${sum_div}`);
}
isDivisible(23);
//EX3

//EX4
/*
Instructions

1.Add the stock and prices objects to your js file.

2.Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

3.Create a function called myBill() that takes no parameters.

4.The function should return the total price of your shoppingList. In order to do this you must follow these rules:
	1.The item must be in stock. (Hint : check out if .. in)
	2.If the item is in stock find out the price in the prices object.

5.Call the myBill() function.

6.Bonus: If the item is in stock, decrease the item’s stock by 1
*/

let stock = { 
	"banana": 6, 
	"apple": 0,
	"pear": 12,
	"orange": 32,
	"blueberry":1
}  

let prices = {    
	"banana": 4, 
	"apple": 2, 
	"pear": 1,
	"orange": 1.5,
	"blueberry":10
} 

let shoppingList = ["banana", "orange", "apple"];

function myBill() {
	let bill = 0;
	for(let i of shoppingList){
		if(i in stock && stock[i] !== 0){
			bill += prices[i];
			stock[i] -= 1;

		}else{
			console.log(`Sorry we are out of ${i}.`)
		}
	}
	return `Your bill is ${bill}$, Thank you for choosing us !!! Have a nice day :)`;
}
console.log(myBill());
//EX4

//EX5
/*
Instructions

Note: Read the illustration (point 4), while reading the instructions

1.Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
	an item price
	and an array representing the amount of change in your pocket.

2.In the function, determine whether or not you can afford the item.
	If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
	If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false

3.Change will always be represented in the following order: quarters, dimes, nickels, pennies.
	A quarters is 0.25
	A dimes is 0.10
	A nickel is 0.05
	A penny is 0.01


4. To illustrate:

After you created the function, invoke it like this:

changeEnough(4.25, [25, 20, 5, 0])

The value 4.25 represents the item’s price.

The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.

The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)


Examples

changeEnough(14.11, [2,100,0,0]) => returns false
changeEnough(0.75, [0,0,20,5]) => returns true
*/

function changeSum(pocket){

	let changeValue =[0.25, 0.10, 0.05, 0.01]
	let sum = 0;

	for(let i in pocket){
		sum += pocket[i] * changeValue[i];
	}
	return sum;
}

function changeEnough(itemPrice, amountOfChange){

	if(changeSum(amountOfChange) >= itemPrice){
		return true;
	}
	else{
		return false;
	}
}
console.log(changeEnough(4.25, [25, 20, 5, 0])); //=> true
console.log(changeEnough(14.11, [2,100,0,0])); // => false
console.log(changeEnough(0.75, [0,0,20,5])); // => true
//EX5

//EX6
/*
Instructions 

Let’s create functions that calculate your vacation’s costs:

1.Define a function called hotelCost().
	It should ask the user for the number of nights they would like to stay in the hotel.
	If the user doesn’t answer or if the answer is not a number, ask again.
	The hotel costs $140 per night. The function should return the total price of the hotel.

2.Define a function called planeRideCost().
	It should ask the user for their destination.
	If the user doesn’t answer or if the answer is not a string, ask again.
	The function should return a different price depending on the location.
		“London”: 183$
		“Paris” : 220$
		All other destination : 300$

3.Define a function called rentalCarCost().
	It should ask the user for the number of days they would like to rent the car.
	If the user doesn’t answer or if the answer is not a number, ask again.
	Calculate the cost to rent the car. The car costs $40 everyday.
		If the user rents a car for more than 10 days, they get a 5% discount.
	The function should return the total price of the car rental.

4.Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

5.Call the function totalVacationCost()

6.Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.

*/

function hotelCost(){

	let stayDuration;
	let cost = 140;

	do{
		stayDuration = prompt("How many nights do you wish to stay at the hotel ?");

		stayDuration = Number(stayDuration);
	}
	while(isNaN(stayDuration));

	return cost * stayDuration;
}

function planeRideCost(){
	
	let destination;
	let numberChecker;

	do{
		destination = prompt("What is your destination ?");
		numberChecker = Number(destination);
	}
	while(!isNaN(numberChecker));

	switch(destination.toLowerCase()){

		case 'london':
		return 183;

		case "paris":
		return 220;

		default:
		return 300;
	}
	
}

function rentalCarCost(){
	
	let rentDays;
	let cost = 40;

	do{
		rentDays = prompt("How many days would you like to rent the car ?");

		rentDays = Number(rentDays);
	}
	while(isNaN(rentDays));

	if(rentDays >= 10){

		return getDiscount(cost * rentDays, 5);
	}
	else{
		return cost * rentDays;
	}
}

function getDiscount(price, percentage){

	let dicount = price;
	price = price / 100 * percentage;
	price = dicount - price;
	return price;
}

function totalVacationCost(){

	let fullPrice = hotelCost() + planeRideCost() + rentalCarCost();

	return `The full cost of your trip will be ${fullPrice}$`; 
}

// console.log(`Your stay will cost ${hotelCost()}$.`);
// console.log(`Your plane ticket will cost ${planeRideCost()}$.`);
// console.log(`Your rental car will cost ${(rentalCarCost())}$.`);
console.log(totalVacationCost());


//EX6