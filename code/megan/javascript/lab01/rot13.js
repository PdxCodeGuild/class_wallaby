const input = prompt('Enter a secret message:')

let alphabetLower = 'abcdefghijklmnopqrstuvwxyz'
let alphabetUpper = alphabetLower.toUpperCase()

let output = []

for (i = 0; i < input.length; i++) {
    letter = alphabetLower.indexOf(input[i]);
    let x = output.push(alphabetLower[(letter + 13) % 26]); // fix; skipping
    console.log(output)
    i++;
}

alert(`Original message: ${input} \nEncrypted message: ${output}`)
console.log(`Original message: ${input} \nEncrypted message: ${output}`)

// test:
// help me = uryc zr