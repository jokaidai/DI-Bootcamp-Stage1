function start(){
	if(pos)
		let box = document.querySelector("#inner");
	let pos = 0;
	if(pos == 350){
		clearInterval(id);
	}
	else{
		let id = setInterval(function(){
			
			pos++
			box.style.top = pos + "px";
		}
	},1)
	}
}