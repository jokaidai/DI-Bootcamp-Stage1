/*
Instructions:

1.Create an input type text that takes/shows only letters. (ie. numbers and special characters won’t be accepted)

	Hint: use one of the following events to remove any character that is not a letter

2.keyup event
	or keypress event
	or keydown event
	or input event

3.Hint : Check out keycodes in Javascript or Regular Expressions
*/

let text = document.querySelector("input");
let btn = document.querySelector("button");
let regex = /^[A-Za-z]+$/

text.addEventListener ("keyup", function(event){
	if(!regex.test(event.key)){
		text.value = text.value.slice(0, -1);

	}
});

btn.addEventListener ("click", function(event){
	text.value = null
});