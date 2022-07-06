/*
Instructions:

1.Create an HTML, CSS and a JS file.

2.In the HTML file
	create a form with one input type="text", and a “Submit” button.
	add an empty div below the form


3.In the js file, you must add the following functionalities:
	1.Create an empty array : let listTasks = [];

	2.Create a function called addTask(). As soon as the user clicks on the button:
		-check that the input is not empty,
		-then add it to the array (ie. add the text of the task)
		-then add it to the DOM, below the form (in the <div class="listTasks"></div>) .
		-Each new task added should have (starting from left to right - check out the image at the top of the page)
			-a “X” button. Use font awesome for the “X” button.
			-an input type="checkbox". The label of the input is the task added by the user.

BONUS I (not mandatory):
1.Change the variable listTasks to an array of task objects.

2.Each new task added to the array should have the properties : task_id, text and done (a boolean - false by default).

3.Every new task object should have a task_id, starting from 0, and a data-task-id attribute, which value is the same as the task_id. Check out data-* attributes here.

4.Create a function named doneTask(), that as soon as the user clicks on the “checkbox” input, the done property should change from false to true in the object, and from black to crossed out red in the DOM.

BONUS II (not mandatory):
1.Create a function named deleteTask(), that as soon as the user clicks on the “X” button, delete that specific task from the array listTasks.
*/

let listTasks = [];