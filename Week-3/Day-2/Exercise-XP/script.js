//EX1
/*
Instructions:


1.Using a DOM property, retrieve the h1 and console.log it.

2.Using DOM methods, remove the last paragraph in the <article> tag.

3.Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

4.Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

5.Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

6.BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

7.BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
*/

let h1 = document.querySelector("h1");
console.log(h1);

h1.addEventListener("mouseover", function(){
	h1.style.fontSize = (Math.floor(Math.random() * 101)) + "px";
});
h1.addEventListener("mouseout", function(){ 
	h1.style.fontSize = "1.5em";
});

let toBeRemove = document.querySelector("article").lastElementChild;
toBeRemove.remove();

let h2 = document.querySelector("h2");
h2.addEventListener("click", function(){
	h2.style.backgroundColor = " red";
});
h2.addEventListener("mouseout", function(){
	h2.style.background = "none";
});

let h3 = document.querySelector("h3");
h3.addEventListener("click", function(){
	h3.style.display = "none";
});
h2.addEventListener("mouseover", function(){
	h3.style.display ='block';
});

let btn = document.querySelector("button");
let clicked;
btn.addEventListener("click", function(){
	if(clicked == true){
		document.body.style.fontWeight = "400";
		btn.innerText = "Bold me !!";
		clicked = false;
	}else{
		document.body.style.fontWeight = "700";
		btn.innerText = "Unbold me !!";
		clicked = true;
	}
});

let p2 = document.querySelector("p").nextElementSibling;
p2.addEventListener("mouseover", function(){
	p2.style.opacity = "0.5";
});
p2.addEventListener("mouseout", function(){
	p2.style.opacity = "1";
});
//EX1

//EX4
/*
Instructions:


In the JS file:

1.Declare a global variable named allBoldItems.

2.Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

3.Create a function called highlight() that changes the color of all the bold text to blue.

4.Create a function called return_normal() that changes the color of all the bold text back to black.

5.Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example
*/

let boldList = document.querySelectorAll("p strong");
let allBoldItems = [];

function getBold_items(){
	let data;
	for(let i = 0; i < boldList.length; i++){
		data = boldList[i].innerText;
		allBoldItems.push(data);
	}
}
function highlight(){
	for(let i = 0; i < boldList.length; i++){
		boldList[i].style.color = "blue";
	}
}
function return_normal(){
	for(let i = 0; i < boldList.length; i++){
		boldList[i].style.color = "black";
	}
}

let pBold = document.querySelectorAll("article")[1].firstElementChild;
pBold.addEventListener("mouseover", function(){
	highlight();
});
pBold.addEventListener("mouseout", function(){
	return_normal();
});

getBold_items();
console.log(allBoldItems);
//EX4

//EX5
/*
Instructions:

1.Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.

2.Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.
*/

let icon = document.querySelector("h4");

icon.addEventListener("click", function(){
	icon.style.fontSize = "36px";
	icon.style.position = "absolute"
});

icon.addEventListener("dblclick", function(){
	icon.style.fontSize = "50px";
	icon.style.position = "relative"
});

icon.addEventListener("mouseover", function(){
	icon.style.backgroundColor = "red";
});

icon.addEventListener("mouseout", function(){
	icon.style.backgroundColor = "White";
});
//EX5