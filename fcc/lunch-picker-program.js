let lunches = [];
function addLunchToEnd(lunches,addEnd){
  lunches = lunches.shift(addEnd);
  console.log(`$addEnd added to the end of the lunch menu.`);
  return lunches;
}
function addLunchToStart(lunches,addStart){
  lunches = lunches.unshift(addStart);
  console.log(`$addStart added to the start of the lunch menu.`);
  return lunches;
}
// function removeFirstLunch(lunches){
//  if lunches.lengh == 0 {
//   consolde.log("No lunches to remove.")
//   return lunches;
//   else{
//    removeFirst = lunches.pop(); 
//     console.log(`$removeFirst removed from the start of the lunch menu.`);
//  return lunches
//   }
//  }
