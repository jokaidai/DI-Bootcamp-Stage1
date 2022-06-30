//---------- Secondary Functions ------------- // 

function getStartNum(){

	let startNum;
	do{
		startNum = prompt("How many bottles do you want to remove !!??");
		startNum = Number(startNum);

		if(isNaN(startNum) == true){
			alert("Hmm ... i need a number man what is your deal ?? drunk already :DD lool !!!");
		}
	}
	while(isNaN(startNum));

	alert("The song started check the console !!! (fn + f12)");

	return startNum;
}

function remove(numOfBottle, numIremove){

	if(numOfBottle == 1){
		console.log(`Take ${numOfBottle} down, pass it around`);
		numOfBottle = 0;

	}else if(numIremove == 1){
		console.log(`Take ${numIremove} down, pass it around`);
		numOfBottle -= numIremove

	}else if(numIremove < numOfBottle){
		console.log(`Take ${numIremove} down, pass them around`);
		numOfBottle -= numIremove

	}else{
		console.log(`Take ${numOfBottle} down, pass them around`);
		numOfBottle = 0;
	}
	return numOfBottle;
}

function starSinging(startNum, numIremove){

	for(let i = 0; i < 4 ; i++){

		switch(i){

			case 0:
			console.log(`${startNum} bottles of beer on the wall`);
			break;

			case 1:
			console.log(`${startNum} bottles of beer`);
			break;

			case 2:
			startNum = remove(startNum, numIremove);
			numIremove ++
			break;

			case 3:
			console.log(`${startNum} bottles of beer on the wall`);
			break;
		}
	}
	console.log(" ");

	if (startNum == 0 || startNum < 0) {
		return;
	}else 
	starSinging(startNum, numIremove);

}

//---------- Secondary Functions ------------- // 

function countTheBeers(){

	let startNum = getStartNum();
	let numIremove = 1;

	starSinging(startNum, numIremove);
}