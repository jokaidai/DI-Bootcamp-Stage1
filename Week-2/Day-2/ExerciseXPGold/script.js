//EX1
/*
Instructions
Hint: Use Switch Case

1.Ask the user which language they speak.

2.Convert the user’s answer to lowercase, so that all the user’s inputs will be accepted in the if statement. For example “english” or “English” or “ENGlish” ect…”

3.Create a few conditions :
	If the user speaks French : display “Bonjour”
	If the user speaks English : display “Hello”
	If the user speaks Hebrew : display “Shalom”
	If the user doesn’t speak any of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’
	*/

	let user_lang = prompt("What language do you speak ?");
	user_lang = user_lang.toLowerCase();

	switch(user_lang){

		case "french":
		console.log("Bonjour");
		break;

		case "english":
		console.log("Hello");
		break;

		case "hebrew":
		console.log("Shalom");
		break;

		default:
		console.log("01110011 01101111 01110010 01110010 01111001 (sorry)")
	}
	//EX1

//EX2
/*
Instructions
1.Ask the user for their grade.

2.If the grade is bigger than 90, console.log “A”

3.If the grade is between 80 and 90 (included), console.log “B”
4.If the grade is between 70(included) and 80 (included), console.log “C”
5.If the grade is lower than 70, console.log “D”
*/

let user_grade = prompt("What is your grade ?");
user_grade = Number(user_grade);

switch(true){

	case user_grade > 90 && user_grade < 101 :
	console.log("A");
	break;

	case user_grade > 80 && user_grade < 91 :
	console.log("B");
	break;

	case user_grade > 70 && user_grade < 81:
	console.log("C");
	break;

	default:
	if(user_grade < 0 || user_grade > 100){

		console.log("Please restrain from entering imaginary grades !!");		
	}else{

		console.log("D");
	}	
}
//EX2

//EX3
/*
Instructions
1.Prompt the user for a string. It must be a verb.
2.If the length of the string is at least 3 and the string doesn’t end with “ing”, add ‘ing’ to the end of the string.
3.If the length of the string is at least 3 and the string ends with “ing” add “ly” to it’s end.
4.If the length of the string is less than 3, leave it unchanged.
*/

let user_verb = prompt("Choose a verb please.");
let verb_length = user_verb.length;
let ing  = /ing/;

if(verb_length < 3){
	console.log(user_verb);
}else if(ing.test(user_verb) == false){
	user_verb = user_verb.concat("ing");
	console.log(user_verb);
}else{
	user_verb = user_verb.concat("ly");
	console.log(user_verb);
}
//EX3