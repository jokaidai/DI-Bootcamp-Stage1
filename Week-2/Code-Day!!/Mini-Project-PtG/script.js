//---------- Secondary Functions ------------- // 

function getUserNum(){

	let userNum;
	do{
		userNum = prompt("Please choose a number between 0 and 10")
		userNum = Number(userNum);

		if(isNaN(userNum)){
			alert("Sorry Not a number, choose a real number this time !!")
		}else if(userNum < 0 || userNum > 10){
			alert("Sorry it’s not a good number, choose one between 1 to 10 this time !!")
		}

	}
	while(userNum < 0 || userNum > 10 || isNaN(userNum));

	return userNum;
}

function getAiNum(){

	let aiNum = Math.floor((Math.random() * 10) + 1);
	return aiNum;
}

//---------- Secondary Functions ------------- // 

function playTheGame() {
	
	if(confirm("Do you want to play with me ?") == false){
		alert("No problem, Goodbye");
	}else{
		let userNum = getUserNum();
		let aiNum = getAiNum();
		compareNumbers(userNum, aiNum);
	}
}
function compareNumbers(userNum, aiNum){

	for(let i = 0; i < 3; i++){

		if(userNum == aiNum){
			alert("WINNER !!");
			return;
		}else if (userNum > aiNum ) {
			if(i == 2){
				break;
			}
			alert("Your number is bigger then mine guess again");
			userNum = getUserNum();
			
		}else{
			if(i == 2){
				break;
			}
			alert("Your number is smaller then mine, guess again");
			userNum = getUserNum();
		}
	}
	alert("Out of chances !!! better luck next time :P");
}