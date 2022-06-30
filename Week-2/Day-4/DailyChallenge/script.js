/*
Instructions

1.Prompt the user for several words (separated by commas).

2.Put the words into an array.

3.Console.log the words one per line, in a rectangular frame as seen below.
*/

function start(){
	comaMaker();
}

function comaMaker(){
	let userWords = [];
	let temp;

	for(i = 0; i < 5; i++){
		temp = prompt("Welcome !!! Give me a few words... )");
		userWords[i] = temp;
	}
	userWords.join(",");
	return userWords;
}
//start();
console.log(comaMaker());