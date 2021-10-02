const input = prompt('Enter a secret message:');

let alphabetLower = 'abcdefghijklmnopqrstuvwxyz';

let output = [];

for (i = 0; i < input.length; i++) {

    letter = alphabetLower.indexOf(input[i]);
    output.push(alphabetLower[(letter + 13) % 26]);
    console.log(output.toString().split(','));
}

let encrypt = output.join('');

alert(`Original message: ${input} \nEncrypted message: ${encrypt}`)
console.log(`Original message: ${input} \nEncrypted message: ${encrypt}`)