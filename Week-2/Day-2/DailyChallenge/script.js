/*
Instructions

	1.Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
	For example, “The movie is not that bad, I like it”.

	2.Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).

	3.Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).

	4.If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
	For example, the result here should be : “The movie is good, I like it”

	5.If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.
	*/

	let sentence = prompt("Enter a sentence please.");  
	let wordNot = sentence.indexOf("not") + 4;
	let wordBad = sentence.indexOf("bad") + 4;
	let newSentence = sentence;

	if(wordNot > 4  && wordBad > wordNot){

		newSentence = sentence.replace("not", "good");
		let sentenceBeg = newSentence.substring(0, wordNot);
		let sentenceEnd = newSentence.substring(wordBad, newSentence.length);
		newSentence = sentenceBeg.concat(sentenceEnd);

		console.log(newSentence);
	}else{

		console.log(sentence);
	}


	//let newSentence = sentence.replace("not", "good");
	//console.log(newSentence);
