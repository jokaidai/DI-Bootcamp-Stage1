//---------- Secondary Functions ------------- // 

function getUserNum(){

	let userNum;
	do{
		userNum = prompt("Please choose a number between 0 and 10")
		userNum = Number(userNum);

		if(isNaN(userNum)){
			alert("Haha very funny !! it’s not a number, choose a real number this time !!")
		}else if(userNum < 0 || userNum > 10){
			alert("Haha very funny !! it's not a good number, choose one between 0 to 10 this time !!")
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

function compareNumbers(userNum, aiNum){

	for(let i = 0; i < 3; i++){

		if(userNum == aiNum){
			alert("CHEATER !!! Stop checking the console debbuger to check my variable !!! ");
			return;
		}else if (userNum > aiNum ) {
			if(i == 2){
				break;
			}
			alert("YOU LOOSE !! Your number is bigger then mine !! Try again looser.");
			userNum = getUserNum();
			
		}else{
			if(i == 2){
				break;
			}
			alert("YOU LOOSE !! Your number is smaller then mine !! Try again looser.");
			userNum = getUserNum();
		}
	}
	alert("Out of chances :P !!! Wow you are really bad at that game ...");
}

function playTheGame() {
	
	if(confirm("Do you want to be destroyed by me at a guessing game ?") == false){
		alert("Then why did you click the button !!! idiot ...");
	}else{
		let userNum = getUserNum();
		let aiNum = getAiNum();
		compareNumbers(userNum, aiNum);
	}
}