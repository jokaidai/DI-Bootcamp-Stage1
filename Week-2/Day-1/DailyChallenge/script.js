//VAR
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

//VAR

console.log("====Ex1===="+"")

//EX1
fruits.shift();
fruits.sort();
fruits.push("kiwi");
fruits.splice(0, 1);
fruits.reverse();
console.log(fruits);
//EX1

console.log("====Ex2===="+"")

//EX2
let oranges = moreFruits[1][1][0];
console.log(oranges);
//EX2