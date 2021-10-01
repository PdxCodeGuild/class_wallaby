const input = prompt('Enter a secret message:');

let alphabetLower = 'abcdefghijklmnopqrstuvwxyz';
let alphabetUpper = alphabetLower.toUpperCase();
// how to account for uppercase, lowercase, and spaces?

let output = [];

for (i = 0; i < input.length; i++) {
    letter = alphabetLower.indexOf(input[i]);
    output.push(alphabetLower[(letter + 13) % 26]);
    // output.join(',');
    console.log(output);
}

// convert array into string
// console.log(output.join(','))


alert(`Original message: ${input} \nEncrypted message: ${output}`)
console.log(`Original message: ${input} \nEncrypted message: ${output}`)

// test:
// hello = uryyb