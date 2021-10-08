//UNIT CONVERTER
const units = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000,
    'yards': .9144,
    'inches': .0254

}
let distance = parseInt(prompt('Enter a distance'));
let unit1 = prompt('Select the unit of your distance');
let unit2 = prompt('Select a unit to convert your distance in to !');

let nums = units[unit1]
let nums2 = units[unit2]
console.log(unit1, nums)
console.log(unit2, nums2)

function math(nums, nums2) {

    total = distance * nums
    convert = total / nums2
    return (convert)
}
let = math(nums, nums2)

console.log ( distance + ' ' + unit1 + ' ' + 'is' + ' ' + x  + ' ' + unit2)
//------------------------------------------------------------------------------------------



