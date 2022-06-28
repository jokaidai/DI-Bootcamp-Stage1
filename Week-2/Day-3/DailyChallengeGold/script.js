/*
Instructions


1.Using the .toString() method convert the array to a string.

2.Using the .join()method convert the array to a string. Try passing different values into the join.
	Eg .join(“+”), .join(” “), .join(“”)

3.Bonus : To do this Bonus look up how to work with nested for loops
	Sort the numbers array in descending order, do so using for loops (Not using built-in sort methods).
	The output should be: [9,8,7,6,5,4,3,2,1,0]
	Hint: The algorithm is called “Bubble Sort”
		Use a temporary variable to swap values in the array.
		Use 2 “nested” for loops (Nested means one inside the other).
		Add comments and console.log the result for each step, this will help you understand.

Requirement: Don’t copy paste solutions from Google
*/

const numbers = [5,0,9,1,7,4,2,6,3,8];
const new_numbers = [];

console.log(numbers.toString());
console.log(numbers.join(" + "));

let highest = 0;
let last_hight = 0;

for(i = 0; i < numbers.length; i++){
	for(j = 0; j < numbers.length; j++){

		if(highest < numbers[j] && i == 0){ //console.log("enter only first ieteration");
		highest = numbers[j];
		last_hight = highest;
		
		}else if(numbers[j] == last_hight || numbers[j] > last_hight){ //console.log("are you blocking ?")	
		continue;

		}else if(highest < numbers[j]){ //console.log("i enter several times");	
		highest = numbers[j];
	}
}
new_numbers[i] = highest;
last_hight = highest;
highest = 0;
}

console.log(new_numbers);