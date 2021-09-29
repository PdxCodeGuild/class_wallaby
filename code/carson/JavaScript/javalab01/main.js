
const units = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000,
    'yards': .9144,
    'inches': .0254

}
let index = prompt({units},'What unit would you like to convert into meters ?');
let nums = units[index]
let distance = parseInt(prompt('How long ?'));
let total = distance * nums

console.log(nums)
console.log(total)
console.log( distance + index + " " + 'into meters is'+ " " + total )


