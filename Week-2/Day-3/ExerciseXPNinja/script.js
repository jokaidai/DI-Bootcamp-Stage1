//EX1 
/*
Instructions: Checking The BMI

Hint:
- You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

1.Create two objects, each object should hold a person’s details. Here are the details:
	1.FullName
	2.Mass
	3.Height

2.Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI) of each person

3.Outside of the objects, create a JS function that compares the BMI of both objects.

4.Display the name of the person who has the largest BMI
*/

let person1 = {
	FullName:"Dwayne 'The Rock' Jhonson",
	Mass: 118,
	Height: 196,
	calc_BMI:function() {
		return (this.Mass / this.Height / this.Height)*10000;	}
	};

	let person2 = {
		FullName:"Kevin Hart",
		Mass: 64,
		Height: 158,
		calc_BMI:function() {
			return (this.Mass / this.Height / this.Height)*10000;
		}
	};
	console.log(person1.calc_BMI());