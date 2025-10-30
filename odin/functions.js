function add7(num) {
    return num + 7;
}

console.log(add7(10));

function multiply(num1, num2) {
    return num1 * num2;
}

console.log(multiply(3, 4));


function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let abcd = "abcd";

console.log(capitalize("abcd"))
console.log(capitalize(abcd))



    // Hole in one calculator
    // const names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"];
    //     console.log(names);
    //     function golfScore(par, strokes) {
    //       // Only change code below this line
    //       if (strokes == 1) {
    //         return names[0];
    //       } else if (strokes <= par - 2) {
    //         return names[1];
    //       } else if (strokes == par - 1) {
    //         return names[2];
    //       } else if (strokes == par) {
    //         return names[3];
    //       } else if (strokes == par + 1) {
    //         return names[4];
    //       } else if (strokes == par + 2) {
    //         return names[5];
    //       } else if (strokes >= par + 3) {
    //         return names[6];
    //       }
        
    //       return "Change Me";
    //       // Only change code above this line
    //     }

