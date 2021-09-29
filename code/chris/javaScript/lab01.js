const unitConverter = (val, fromUnit, toUnit) => {
  let unitTable = {
    ft: {
      m: 0.3048
    },
    mi: {
      m: 1609.34
    },
    m: {
      ft: 0.3084,
      mi: 1/1609.34,
      km: 0.001
    }
  }

  return fromUnit === toUnit ? val : val * unitTable[fromUnit][toUnit] + toUnit || 'Invalid units'
}

// console.log(unitConverter(1600, 'm', 'km'))
const rOI = (expenses, earnings) => {
  return ((earnings - expenses) / expenses)
}

const pick6 = rounds => {
  let cost = rounds * 2;
  let profit = 0;
  let tally = -cost;

  const matchPayout = {
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
  }
  for (let idx = 0; idx < rounds; idx += 1) {
    let obj = {};
    let matches = 0;

    for (let jdx = 0; jdx < 6; jdx += 1) {
      let rn = Math.round(Math.random() * 100)
      obj[rn] ? obj[rn]++ : obj[rn] = 1
      if (obj[rn] > 1) matches++
    }

    // console.log(obj)
    tally += matchPayout[matches] || 0
    profit += matchPayout[matches] || 0

  }
  let roi = rOI(cost, profit)
  let roiStr = `Your ROI is ${roi}`

  return tally < 0 ? `You lost $${Math.abs(tally)}. ${roiStr}`: `You made $${tally}!!!`
}

// console.log(pick6(100000))

const rot13 = (str, rot) => {
  return str.split('').map( el => {
    if (el === ' ')
      return ' '
    else {
      let setter = el.charCodeAt(0) > 96 && el.charCodeAt(0) < 123 ? 97 : 65
      let charCode = (el.charCodeAt(0) - setter + rot) % 26
      if (charCode < 0)
        charCode += 26;
      return String.fromCharCode(charCode + setter)
    }
  }).join('')
}

// console.log(rot13('abcn', 13))
// console.log(rot13('nopa', -13))
// console.log(rot13('abcz', 1))
// console.log(rot13('bcda', -1))
console.log(rot13('zhere Is soMe ranDom sTRing', 1))
console.log(rot13('aifsf Jt tpNf sboEpn tUSjoh', -1))

