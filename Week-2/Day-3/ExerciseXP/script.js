//VAR

//VAR

//EX1
/*
Instructions

Part I - Review About Arrays

1.Write code to remove “Greg” from the people array.

2.Write code to replace “James” to “Jason”.

3.Write code to add your name to the end of the people array.

4.Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

5.Write code to make a copy of the people array using the slice method.
	The copy should NOT include “Mary” or your name.
	Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason", "Yourname"];
	Hint: Check out the documentation for the slice method

6.Write code that gives the index of “Foo”. Why does it return -1 ?

7.Create a variable called last which value is the last element of the array.
	Hint: What is the relationship between the index of the last element in the array and the length of the array?
	*/

	let people = ["Greg", "Mary", "Devon", "James"];
	console.log(people);
	people.shift();
	console.log(people);
	people.pop();
	people.push("Jason");
	console.log(people);
	people.push("Elie");
	console.log(people);
	console.log(people.indexOf("Mary"));
	let copy_people = people.slice(1, people.length - 1);
	console.log(copy_people);
	console.log(people.indexOf("foo")); // return -1 because foo is undefined ... therefore he didnt find it in the array
	let last = people.length - 1;
	console.log(last);

	/*
Part II - Loops

1.Using a loop, iterate through the people array and console.log each person.

2.Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
	Hint: take a look at the break statement in the lesson.
	*/

	for(let i of people){
		console.log(i);
	}

	let i = 0;
	do {
		console.log(people[i]);
		if(people[i] === "Jason"){
			break;
		}
		i++
	}
	while(i < people.length);
//EX1

//EX2
/*
Instructions: Your Favorite Colors

1.Create an array called colors where the value is a list of your five favorite colors.

2.Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .

3.Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
Hint : create an array of suffixes to do the Bonus
*/

let colors = ["Green", "Black", "Cyan", "White", "Orange"];

for (let i in colors) {
	console.log(`My #${Number(i) + 1} choice is ${colors[i]}`);
}

for (let i in colors) {

	switch (i.toString()) {

		case '0':
		console.log(`My ${Number(i) + 1}st choice is ${colors[i]}`);
		break;

		case '1':
		console.log(`My ${Number(i) + 1}nd choice is ${colors[i]}`);
		break;

		case '2':
		console.log(`My ${Number(i) + 1}rd choice is ${colors[i]}`);
		break;

		default:
		console.log(`My ${Number(i) + 1}th choice is ${colors[i]}`);
	}
}
//EX2

//EX3
/*
Instructions

1.Prompt the user for a number.
	Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

2.While the number is smaller than 10 continue asking the user for a new number.
	Tip : Which while loop is more relevant for this situation?
	*/

	let user_num = prompt("Please choose a number greater then 10.");
	user_num = Number(user_num); 

	while(user_num < 10)
	{
		user_num = prompt("Haha very funny now follow the instuction !! choose a number greater then 10.");
		user_num = Number(user_num);
	}
//EX3

//EX4
/*
Instructions:Review About Objects


1.Copy and paste the above object to your Javascript file.

2.Console.log the number of floors in the building.

3.Console.log how many apartments are on the floors 1 and 3.

4.Console.log the name of the second tenant and the number of rooms he has in his apartment.

5.Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
*/

let building = {
	numberOfFloors : 4,
	numberOfAptByFloor :
	{
		firstFloor : 3,
		secondFloor : 4,
		thirdFloor : 9,
		fourthFloor : 2,
	},
	nameOfTenants : ["Sarah", "Dan", "David"],
	numberOfRoomsAndRent: 
	{
		sarah: [3, 990],
		dan :  [4, 1000],
		david : [1, 500],
	},
}

console.log(`There is ${building.numberOfFloors} floors in the building.`);
console.log(`There is ${building.numberOfAptByFloor.firstFloor} apartments in the first floor, and ${building.numberOfAptByFloor.thirdFloor} in the third.`);
console.log(`${building.nameOfTenants[1]} have ${building.numberOfRoomsAndRent.dan[0]} rooms in his apartment.`);

if(building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]){
	building.numberOfRoomsAndRent.dan[1] = 1200;

}
console.log(`The rent of dan is now ${building.numberOfRoomsAndRent.dan[1]}`);
//EX4

//EX5
/*
Instructions

1.Create an object called family with a few key value pairs.

2.Using a for in loop, console.log the keys of the object.

3.Using a for in loop, console.log the values of the object.
*/

let family = {
	mom: "Danielle",
	dad: "Patick",
	brother: "Pascal",
	biger_sis: "Valerie",
	big_sis: "Deborah",
};

for(i in family){
	console.log(i);
	console.log(family[i]);
}
//EX5

//EX6
/*
Instructions

1.Given the object under and using a for loop, console.log “my name is Rudolf the raindeer”
*/

let details = {
	my: 'name',
	is: 'Rudolf',
	the: 'raindeer'
}

let sentence = "";
for(i in details){
	sentence += (i) + " ";
	sentence += (details[i]) + " ";
}
console.log(sentence);
//EX6

//EX7
/*
Instructions

1.A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
	Hint: a string is an array of letters

2.Console.log the name of their secret society. The output should be “ABJKPS”
*/

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let secret_society = [""];

for(i in names){
	secret_society[i] = names[i].charAt(0);
}

secret_society.sort();
console.log(secret_society.join(""));
//EX7