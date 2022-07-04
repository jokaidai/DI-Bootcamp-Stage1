//EX1
/*
Instructions:

Create a structured HTML file, and add the code below in the body.

In a JS file, write a JavaScript function to add rows to a table. Use the code below as a base
*/
//EX1

function insertData(){

	let rowCount = document.querySelectorAll("tr").length + 1; 

	let tr = document.createElement("tr");
	let td;
	let data;

	for(let i = 1; i < 3; i++){

		td  = document.createElement("td");
		data = document.createTextNode(`Row${rowCount} cell${i}`)

		td.appendChild(data);
		tr.appendChild(td);
	}
	return tr;
}

function insertRow(){

	let table = document.querySelector("#sampleTable tbody");
	let tr = insertData();

	return table.appendChild(tr);
}

//EX2
/*
Instructions:

Add a few event listener to the button. The event listeners should change the style of the button
*/

// ----- Secondary Functions -----

function RespondMouseOver(btnStyle) { 
	btnStyle.style.fontSize = "50px";
	btnStyle.style.backgroundColor = "red";
	btnStyle.style.borderRadius = "15px";

}
function RespondMouseOut(btnStyle){
	btnStyle.style.fontSize = "16px";
	btnStyle.style.backgroundColor = "darkGray";
	btnStyle.style.borderRadius = "0px";
}
// ----- Secondary Functions -----

let btnStyle = document.querySelector("#jsstyle");

btnStyle.addEventListener("mouseover", function(){
	RespondMouseOver(btnStyle);
});
btnStyle.addEventListener("mouseout", function(){
	RespondMouseOut(btnStyle);
}); 

//EX2

//EX3
/*
Instructions:

Add a click event listener to the div

Add a few event listeners to the button. With at least one click event. The event listeners should change the style of the button

Check how the propagation works and try to prevent it
*/
let btnClick = document.querySelector("#jsstyle");
let btnClick1 = document.querySelector("#propagationWall");
let btnClick2 = document.querySelector("#propagationSky");

btnClick.addEventListener("click", clickGreen); 
btnClick1.addEventListener("click", clickBlue); 
btnClick2.addEventListener("click", clickOrange);

function clickGreen(event){
	
	btnClick.style.backgroundColor = "green";
	alert("green");
	event.stopPropagation();
}

function clickBlue(){

	btnClick.style.backgroundColor = "blue";
	alert("blue");
}

function clickOrange(){
	
	btnClick.style.backgroundColor = "orange";
	alert("orange");
}
//EX3