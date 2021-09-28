// Version 1

const distance = prompt('What is the distance in feet?')

// let conversion = `${distance} feet is ${...}`
alert('conversion')
console.log(conversion)

// Version 2

const distance = prompt('What is the distance?')
const units = prompt('What are the units (ft, mi, m, or km)?')

conversion_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
}

// Version 3

const units = prompt('What are the units (ft, mi, m, km, yd, or in)?')

const conversionFactor = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

// Version 4