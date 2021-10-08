
//Pick6
payout = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}
let expenses = 0
let winning = []
let ticket = []
let totalLoop = 0
const control = 99999
let earnings = 0

function pick6() {
    num = Math.round(Math.random() * 9)
    winning.push(num)
}

for (let i = 1; i <= 6; ++i) { pick6() }
console.log('Winning Ticket :' + ' ' + winning)

function playerPick() {
    num = Math.round(Math.random() * 9)
    ticket.push(num)
}

for (let i = 1; i <= 6; ++i) { playerPick() }

let matches = winning.filter(element => ticket.includes(element));
let totalMatch = matches.length
let prize = payout[totalMatch]


while (totalLoop <= control) {
    playerPick()
    totalLoop++;
    expenses += 2
    earnings += prize
    roi = (earnings - expenses) / expenses

}




console.log('Earnings : $' + earnings)
console.log('Expenses : $' + expenses)
console.log('Return on investment : $' + roi)