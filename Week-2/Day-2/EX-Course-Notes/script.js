//VAR

//EX2
let a = 2 + 2;
//EX2

//EX3
let b = 2 + 2;
//EX3

//EX4
let user0 = {
	userName: "Jokaidai",
	password: "3713F@",
	timeline:"",
};
let user1 = {
	userName: "Ar@fel",
	password: "ben10",
	timeline:"",
};
let user2 = {
	userName: "Zeavan",
	password: "@Cf789523311ihaveabadasspasswordyou'lneverhackit!!",
	timeline:"",
};
let database = [user0];
let newsfeed = [user0, user1, user2]
//EX4

//VAR

//EX1
let userAge = prompt("how old ar you ?");
if(userAge == 18){
	alert("Congratulations on your first year of driving. Enjoy the ride!")
}else if(userAge > 18){
	alert("Powering On. Enjoy the ride!")
}else{
	alert("Sorry, you are too young to drive this car. Powering off")
}
//EX1

//EX2
switch (a) {
	case 3:
	alert( 'Too small' );
	break;
	case 4:
    alert( 'Exactly!' );  //(correct)
    break;
    case 5:
    alert( 'Too large' );
    break;
    default:
    alert( "I don't know such values" );
}
//EX2

//EX3
switch (b) {
	case 4:
    alert('Right!'); //(correct)
    break;

  case 3: // (*) grouped two cases
  case 5:
  alert('Wrong!');
  alert("Why don't you take a math class?");
  break;

  default:
  alert('The result is strange. Really.');
}
//EX3

//EX4
console.log(user0);
console.log(database);
console.log(newsfeed);
//EX4