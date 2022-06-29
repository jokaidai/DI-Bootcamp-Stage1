//EX1
/*
1. Create a structured html file linked to a js file

2. Write a JS function that takes a parameter: myAge

3. Console.log the age of my mum and my dad (my mum is twice my age, and my dad is 1.2 the age of my mum)

4. Call the function
*/

function myAge(age){
	let mum_age = age * 2
	let dad_age = mum_age * 1.2
	dad_age = Math.round(dad_age);

	console.log(`The age of my mum and my dad is: ${mum_age} and ${dad_age} respectively.`);
}
myAge(29);
//EX1

//EX2
/*
1. Create a structured html file linked to a js file

2. Write a JS function that takes a parameter: myAge

3. Return the age of my mum (my mum is twice my age)

4. Call the function

5. Console.log the age of my mum
*/

function myAge2(age){
	let mum_age = age * 2;
	return mum_age; 
}

let result = myAge2(29);
console.log(result);
//EX2