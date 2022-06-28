/*
Instructions

1.Write a JavaScript program that recreates the pattern below.

2.Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out “nested for loops” on Google).

3.Do this Daily Challenge by youself, without looking at the answers on the internet.

*  
* *  
* * *  
* * * *  
* * * * *
* * * * * *

*/
//ONE LOOP

for(let i = 1; i < 6; i++){
	console.log("* ".repeat(i));
}

//NESTED LOOP

for (let i = 0; i < 6; i++) {
	for (let j = 0; j <= i; j++) {
		console.log("* ".repeat(i));
	}
}