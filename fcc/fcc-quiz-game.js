
let questions = [
	{
		category: "location",
		question: "Where are you from?",
		choices: ["east", "west", "central"],
		answer: "west"
	},
	{
		category: "food",
		question: "What’s your favorite fruit?",
		choices: ["apple", "banana", "orange"],
		answer: "banana"
	},
	{
		category: "animals",
		question: "Which animal barks?",
		choices: ["cat", "dog", "cow"],
		answer: "dog"
	},
	{
		category: "colors",
		question: "What color is the sky?",
		choices: ["blue", "green", "yellow"],
		answer: "blue"
	},
	{
		category: "math",
		question: "What is 2 + 2?",
		choices: ["3", "4", "5"],
		answer: "4"
	}
];

function getRandomQuestion(questions) {
	let randomIndex = Math.floor(Math.random() * questions.length);
	return questions[randomIndex];
}

function getRandomComputerChoice(choices) {
	let randomIndex = Math.floor(Math.random() * choices.length);
	return choices[randomIndex];
}

function getResults(question, computerChoice) {
	if (computerChoice === question.answer) {
		return "The computer's choice is correct!";
	} else {
		return `The computer's choice is wrong. The correct answer is: ${question.answer}`;
	}
}

let randomQuestion = getRandomQuestion(questions);
console.log("Question:", randomQuestion.question);

let computerChoice = getRandomComputerChoice(randomQuestion.choices);
console.log("Computer chose:", computerChoice);

let result = getResults(randomQuestion, computerChoice);
console.log(result);
