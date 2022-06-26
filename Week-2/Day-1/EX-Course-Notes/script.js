// VAR

// EX-1

let addressNumber = '22';
let addressStreet = 'Ushisskin';
let country = 'Israel';
let globalAddress = `${addressNumber} ${addressStreet} ${country}`;

// EX-1

// EX-2

let yOb = '1993';
let fY = '2077';
let fA = fY - yOb;

// EX-2

// EX-3

let pet = ["cat", "dog", "fish", "rabbit", "cow"];

//EX-3

// VAR

console.log(`I live in ${globalAddress} :p`); //EX-1
console.log(`I will be ${fA} in ${fY} :P`); //EX-2

//EX-3

console.log(pet);
console.log(pet[1]); 
pet[3] = "horse";
console.log(pet);
console.log(pet.length);

//EX-3

//EX-3a

alert("Hello !!!");
let wru = prompt("What is your name ?", 'Elie');
confirm(`Your name is ${wru}`);
if(wru == "Elie"){
	alert("Your the BOSS ;)");
}
else{
	alert("GET OFF THIS WEBSITE YOU HACKER !!")
}
//EX-3a