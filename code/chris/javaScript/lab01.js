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

console.log(unitConverter(1600, 'm', 'km'))

