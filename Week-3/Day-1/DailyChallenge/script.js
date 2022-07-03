/*
Instruction:

1.Create an array which value is the planets of the solar system.

2.For each planet in the array, create a <div> using createElement. This div should have a class named "planet".

3.Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).

4.Finally append each div to the <section> in the HTML (presented below).

5.Bonus: Do the same process to create the moons.
	Be careful, each planet has a certain amount of moons. How should you display them?
	Should you still use an array for the planets ? Or an array of objects ?
	*/

	let solarSys = ["Earth", "Mars", "Mercury", "Venus", "Jupiter", "Saturn", "Uranus", "Neptune"];
	
	for (let i in solarSys){
		let addPlanet = document.createElement("div");
		addPlanet.innerText = solarSys[i];
		addPlanet.classList.add("planet");
		addPlanet.style.backgroundColor = `rgb(${i * 40}, ${i * 26}, ${i * 84})`;
		document.querySelector(".listPlanets").appendChild(addPlanet);
	}