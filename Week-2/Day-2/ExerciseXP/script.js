//VAR

//EX1
let x = 26;
let y = 13;
//EX1

//EX2
let newDog = "Chihuahua";
//EX2

//EX4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let conected = users.length;
//EX4

//VAR

//EX1
/*Instructions
1.Create 2 variables, x and y. Each of them should have a different numeric value.
2.Write an if/else statement that checks which number is bigger.*/

// if(x > y){
// 	console.log("X is bigger!")
// }else if(y>x){
// 	console.log("Y is bigger!")
// }else{
// 	console.log("X and Y are equals!")
// }
// //EX1

//  //EX2
//  /*Instructions
// 1.Create a variable called newDog where it’s value is “Chihuahua”.
// 2.Check and display how many letters are in newDog.
// 3.Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
// 4.Check if the variable newDog is equal to “Chihuahua”
// 		if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// 		else, console.log ‘I dont care, I prefer cats’
// 			*/

// 		console.log(newDog.length);
// 		console.log(newDog.toUpperCase());
// 		console.log(newDog.toLowerCase());
// 		if(newDog == "Chihuahua"){
// 			console.log("I love Chihuahuas, it’s my favorite dog breed")
// 		}else{
// 			console.log("I dont care, I prefer cats")
// 		}
// //EX2

// //EX3
// /*
// Instructions
// 1.Prompt the user for a number and save it to a variable.
// 1.Check whether the variable is even or odd.
// 		If it is even, display: “x is an even number”. Where x is the actual number the user chose.
// 		If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.
// 		*/

// 		let user_num = prompt("Define the value of x please.");
// 		user_num = Number(user_num);

// 		if (user_num % 2 == 0){
// 			console.log("x is an even number")
// 		}else{
// 			console.log("x is an odd number")
// 		}
// //EX3

//EX4
/*
Instructions
1.Using the array above, console.log the number of users that are connected to the group chat based on the following rules:
		If there is no users (the users array is empty), console.log “no one is online”.
		If there is 1 user, console.log “<name_user> is online”.
		If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
		If there are more than 2 users, console.log the first two names in the users array and the number of additional users online
		*/

		switch (conected){

			case 0:
			console.log("no one is online");
			break;

			case 1:
			console.log(`${users[0]} is online`);
			break;

			case 2:
			console.log(`${[users[0], users[1]].join(' and ')} are online`);
			break;

			default:
			if(conected > 2){
				console.log(`${[users[0], users[1]].join(' and ')} + ${conected - 2} others are online.`);
			}
		}
//EX4