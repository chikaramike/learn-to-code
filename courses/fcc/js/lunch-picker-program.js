let lunches = [];

function addLunchToEnd(lunchArray,lunchItem) {
  lunchArray.push(lunchItem);
  console.log(`${lunchItem} added to the end of the lunch menu.`);
  return lunchArray;
}

function addLunchToStart(lunchArray,lunchItem) {
  lunchArray.unshift(lunchItem);
  console.log(`${lunchItem} added to the start of the lunch menu.`);
  return lunchArray;
}

function removeLastLunch(lunchArray) {
  if (lunchArray.length === 0) {
    console.log("No lunches to remove.");
    } else {
    const removedItem = lunchArray.pop(); 
    console.log(`${removedItem} removed from the end of the lunch menu.`);
  }
  return lunchArray; 
}
function removeFirstLunch(lunchArray) {
  if (lunchArray.length === 0) {
    console.log("No lunches to remove.");
  } else {
    const removedItem = lunchArray.shift(); // Remove the first element and store it
    console.log(`${removedItem} removed from the start of the lunch menu.`);
  }
  return lunchArray; // Return the updated (or original, if empty) array
}

function getRandomLunch(lunchArray) {
  if (lunchArray.length === 0) {
    console.log("No lunches available.");
  } else {
    // Generate a random index within the array's bounds
    const randomIndex = Math.floor(Math.random() * lunchArray.length);
    // Get the lunch item at the random index
    const randomLunchItem = lunchArray[randomIndex];
    console.log(`Randomly selected lunch: ${randomLunchItem}`);
  }
}

function showLunchMenu(lunchArray) {
  if (lunchArray.length === 0) {
    console.log("The menu is empty.");
  } else {
    // Join all elements with ", " to form the menu string
    console.log(`Menu items: ${lunchArray.join(", ")}`);
  }
}

addLunchToEnd(lunches, "Pizza");
addLunchToEnd(lunches, "Burger");
addLunchToStart(lunches, "Salad");
console.log(lunches); // ["Salad", "Pizza", "Burger"]
