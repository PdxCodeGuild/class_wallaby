// Version 1

// const distance = prompt('What is the distance in feet?')
// alert(`${distance} feet is ${(distance * 0.3048)} meters.`)
// console.log(`${distance} feet is ${(distance * 0.3048)} meters.`)

// Version 2

// const distance = prompt('What is the distance?')
// console.log(distance)

// const units = prompt('What are the units (ft, mi, km)?')
// console.log(units)

// const conversionFactor = {
//     'ft': 0.3048,
//     'mi': 1609.34,
//     'm': 1,
//     'km': 1000,
// }

// alert(`${distance} ${units} is ${(distance * conversionFactor[units])} meters`)
// console.log(`${distance} ${units} is ${(distance * conversionFactor[units])} meters`)

// Version 3

// conversionFactor.add { // not correct; fix
//     'yd': 0.9144,
//     'in': 0.0254,
// }

const distance = prompt('What is the distance?')
console.log(distance)

const units = prompt('What are the units (ft, mi, km, yd, in)?')
console.log(units)

const conversionFactor = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

alert(`${distance} ${units} is ${(distance * conversionFactor[units])} meters`)
console.log(`${distance} ${units} is ${(distance * conversionFactor[units])} meters`)


// Version 4