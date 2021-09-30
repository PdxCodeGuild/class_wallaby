// Version 1

// const distance = prompt('What is the distance in feet?')
// alert(`${distance} feet is equal to ${(distance * 0.3048)} meters.`)
// console.log(`${distance} feet is equal to ${(distance * 0.3048)} meters.`)

// Version 2

// const distance = prompt('What is the distance?')
// console.log(distance)

// const units = prompt('What are the units (feet, miles, kilometers)?')
// console.log(units)

const conversionFactor = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilmeters': 1000,
}

// alert(`${distance} ${units} is equal to ${(distance * conversionFactor[units])} meters.`)
// console.log(`${distance} ${units} is equal to ${(distance * conversionFactor[units])} meters.`)

// Version 3

conversionFactor.yards = '0.9144'
conversionFactor.inches = '0.0254'

// const distance = prompt('What is the distance?')
// console.log(distance)

// const units = prompt('What are the units (feet, miles, kilometers, yards, inches)?')
// console.log(units)

// alert(`${distance} ${units} is equal to ${(distance * conversionFactor[units])} meters.`)
// console.log(`${distance} ${units} is equal to ${(distance * conversionFactor[units])} meters.`)

// Version 4

const distance = prompt('What is the distance?')
console.log(distance)

const inputUnits = prompt('What are the input units (feet, miles, meters, kilometers, yards, inches)?')
console.log(inputUnits)

const outputUnits = prompt('What are the output units (feet, miles, meters, kilometers, yards, inches)')
console.log(outputUnits)

alert(`${distance} ${inputUnits} is equal to ${(distance * conversionFactor[inputUnits] / conversionFactor.meters)} ${outputUnits}.`)
console.log(`${distance} ${inputUnits} is equal to ${(distance * conversionFactor[inputUnits] / conversionFactor.meters)} ${outputUnits}.`)