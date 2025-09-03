var name = prompt('What is your name?');

alert('Hello, ' + name + '! Welcome to my website.');

var dob = prompt('What is your date of birth? (YYYY-MM-DD)');
var birthDate = new Date(dob);
var today = new Date();
var age = today.getFullYear() - birthDate.getFullYear();
var monthDiff = today.getMonth() - birthDate.getMonth();
if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
    age--;
}

alert('You are ' + age + ' years old.');    


    