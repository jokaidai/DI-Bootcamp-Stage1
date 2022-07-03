//EX1
/*
Instructions:

1.Using Javascript:
    -Retrieve the div and console.log it
    -Change the name “Pete” to “Richard”.
    -Change each first name of the two <ul>'s to your name.
    -Delete the <li> that contains the text node “Sarah”.

2.Bonus - Using Javascript:
    -Add a class called student_list to both of the <ul>'s.
    -Add the classes university and attendance to the first <ul>.
    */

   //  console.log(document.getElementById("container"));
   //  document.querySelector(".list").children[1].textContent = "Richard";

   //  let liList = document.getElementsByTagName("ul");
   //  for(let i = 0; i < liList.length; i++){
   //     liList[i].firstElementChild.textContent = "Elie";
   //     liList[i].classList.add("student_list");
   // }
   // liList[0].classList.add("university");
   // liList[0].classList.add("attendance");

   // let list2 = document.getElementsByClassName("list")[1];
   // list2.removeChild(list2.children[1]);
//EX1

//EX2
/*
Instructions:

1.Add a “light blue” background color and some padding to the <div>.

2.Do not display the <li> that contains the text node “John”.

3.Add a border to the <li> that contains the text node “Pete”.

4.Change the font size of the whole body.

5.Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).
*/

// let users = document.getElementsByTagName("div")[1];
// console.log(users);
// users.style.backgroundColor = "lightBlue";
// users.style.padding = "5px";

// liList[2].firstElementChild.style.display = "none"; //liList is a var from the first exercise that stock all the ul.
// liList[2].firstElementChild.nextElementSibling.style.border = "solid black 1px";

// document.body.style.fontSize = "36px";

// for(let i = 0; i < liList.length; i++){

//  if(liList[i].previousElementSibling.style.backgroundColor == "lightBlue")
//     alert(`Hello ${liList[i]} and ${liList[i].nextElementSibling}`);
// }
//EX2

//EX3
/*
Instructions:

1.In the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

2.We are going to add a new <li> to the <ul>.
    1-First, create a new <li> tag (use the createElement method).
    2-Create a new text node with “Logout” as its specified text.
    3-Append the text node to the newly created list node (<li>).
    4-Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

3.Bonus
    Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).
    */

    // let ulList = document.querySelector("div ul");
    // ulList.parentElement.setAttribute("id", "socialNetworkNavigation");

    // let newLi = document.createElement("li");
    // let textNode = document.createTextNode("Logout");
    // newLi.appendChild(textNode);
    // ulList.appendChild(newLi);

    // console.log(ulList.firstChild.nextElementSibling.textContent);
    // console.log(ulList.lastChild.textContent);
//EX3

//EX4
/*
Instructions:

The point of this challenge is to display a list of two books on your browser.

1.In the body of the HTML page, create an empty div:
    <div class="listBooks"></div>

2.In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
    title,
    author,
    image : a url,
    alreadyRead : which is a boolean (true or false).

3.Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

4.Requirements : All the instructions below need to be coded in the js file:

    1.Using the DOM, render the books inside an HTML table (the HTML table must be added to the <div> created in part 1).

    For each book :

        You have to display the book’s title and the book’s author.
        Example: HarryPotter written by JKRolling.

        The width of the image has to be set to 100px.

        If the book is already read. Set the color of the book’s details to red.
        */
//EX4