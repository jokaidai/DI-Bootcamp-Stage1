/*
Instructions

1.Prompt the user for several words (separated by commas).

2.Put the words into an array.

3.Console.log the words one per line, in a rectangular frame as seen below.
*/

// a few things to correct First the user should be asked only one time for words separated by comas and then stored in a variable


function start(){
	comaMaker();
}

// remember you should return a frame of * for the words.
// try to think of how in every iteration you would add * and spaces in the rigth side and left side
// depending on the length of every word
// also you should check first the longer word of the array of words give by the user to understand
// wich is the size of the frame you will be working to
// let me know when you redo the exercise i will correct it again.

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