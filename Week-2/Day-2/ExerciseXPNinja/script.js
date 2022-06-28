/*
Instruction
1.Given the years two people were born, find the date when the younger one is exactly half the age of the older.
	
	Notes: The dates are given in the format YYYY

	*/

//EX1
let older = prompt("Oldest among you please enter you year of birth.");
older = Number(older);
let younger = prompt("Now the younger ...");
younger = Number(younger);
alert("Thank you ! calculating check the console ...");

let age_gap = younger - older;
let half_age = age_gap * 2;
half_age = older + half_age;
console.log(`The person born in ${younger} will be exactly half the age of the person born in ${older} in ${half_age}.`);
//EX1