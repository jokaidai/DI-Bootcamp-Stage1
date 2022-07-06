//EX1
/*
Instructions:

Part I
1.In your Javascript file, using setTimeout, call a function after 2 seconds.

2.The function will alert “Hello World”.

Part II
1.In your Javascript file, using setTimeout, call a function after 2 seconds.

2.The function will add a new paragraph <p>Hello World</p> to the <div id="container">

Part III
1.In your Javascript file, using setInterval, call a function every 2 seconds.

2.The function will add a new paragraph <p>Hello World</p> to the <div id="container">.

3.The interval will be cleared (ie. clearInterval), when the user will click on the button.

4.Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.
*/

// (uncomment from here for ex 1)

// let container = document.querySelector("#container");

// function pMaker(){
// 	let newP = document.createElement("p");
// 	let data = document.createTextNode("Hello World");

// 	setTimeout(function(){
// 		newP.appendChild(data);
// 		container.appendChild(newP); 
// 	}, 2000);
// }

// let id;
// let counter = 0;
// function pRepeat(){
// 	id = setInterval(function(){
// 		if(counter > 4){
// 			stopRepeat();
// 		}else{
// 			pMaker();
// 		}
// 		counter++
// 	}, 2000);
// }

// function stopRepeat(){
// 	clearInterval(id);
// }

// pRepeat();
//EX1

//EX2
/*
Instructions:

1.In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.

The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
Hint : use clearInterval as soon as the box reaches the right end side of the container
Hint : check out the demonstration in the Course Noted named JS Functions
*/
// uncoment from here for ex2

// let redBox = document.querySelector("#animate");

// function myMove(){
// 	let pos = 0;

// 	let id = setInterval(function(){
// 		if(pos == 350){
// 			clearInterval(id);
// 		}else{
// 			pos++
// 			redBox.style.left = pos + "px";
// 		}
// 	},1);
// }
//EX2

//EX3
/*
Instructions:

1.In your Javascript file add the functionality which will allow you to drag the box and drop it into the target. Check out the Course Notes named DOM animations.
*/

function dragStart(event){
	event.dataTransfer.setData("RedBox", event.target.id);
}

function dragOver(event){
	event.preventDefault();
}
function dragDrop(event){
	event.preventDefault();
	let data = event.dataTransfer.getData("RedBox");
	let redBox = document.getElementById(data);
	event.target.appendChild(redBox);
}
//EX3