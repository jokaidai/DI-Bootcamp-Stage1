// col/row of the sidebar
let color_col = 3;
let color_row = 8;
let color_count = color_col * color_row;
// column of the sidebar

// col/row of the canvas
let main_col = 60;
let main_row = 50;
let main_count = main_col * main_row;
// col/row of the canvas

//general var
let penColor;
let mouseDown;
let canvas = [];
//general var

//container declaration
let sidebar = document.getElementById('sidebar');
let main = document.querySelector('#main');
let body = document.querySelector("body");
let btn = document.querySelector("button");
//container declaration

//mouse down check
body.addEventListener("mousedown", function(){
  mouseDown = true;
});

body.addEventListener("mouseup", function(){
  mouseDown = false;
});
//mouse down check

//clear
btn.addEventListener("click", function(){
  for(i of canvas){
    i.style.backgroundColor = '';
  }
});
//clear

//sidebar creation (with added event)
for (let i = 0; i < color_count; i++) {
  let div = document.createElement('div');
  div.style.backgroundColor = generateRandomColor();
  sidebar.appendChild(div);
  div.addEventListener("click",function(){
    penColor = div.style.backgroundColor;
  });
}
//sidebar creation (with added event)

//canvas creation (with added event)
for (var i = 0; i < main_count; i++) {
  let div = document.createElement("div");
  main.appendChild(div);
  div.addEventListener("mouseover", function(){
    if(mouseDown){
     div.style.background = penColor;
   }
 });
  canvas.push(div); //each div is added with is events to the canvas arr to use them easily later
}
//canvas creation (with added event)

function generateRandomColor(){
  let letters = '0123456789ABCDEF'
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)]
  }
  return color;
}
