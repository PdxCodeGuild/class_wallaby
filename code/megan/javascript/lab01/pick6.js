function pick6() {

    let ticket = [];
    let min = 1;
    let max = 99;

    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min))
    };

    for (let i = 0; i < 6; i++) {
        ticket.push(getRandomInt(min, max));
    }

    return ticket
}

const winningTicket = pick6()

function compareMatches(winning, ticket) {

    let matches = 0;

    for (let i = 0; i < winning.length; i++) {
        if (winning[i] === ticket[i]) {
            matches += 1;
        }
    }

    return matches
}

function winningsFunction() {

    const winningsObject = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    }

    let expenses = 0;
    let earnings = 0;
    let balance = 0;
    let roi = 0;

    for (let i = 0; i < 100000; i++) {
        expenses += 2;
        earnings += (winningsObject[compareMatches(winningTicket, pick6())]);
        balance -= 2;
        roi += (earnings - expenses) / expenses;
    }

    alert(`After 100,000 tries, your earnings equal $${earnings}. \nYour expenses equal $${expenses}. \nYour return on investment(ROI) is $${roi}.`)
    return (`After 100,000 tries, your earnings equal $${earnings}. \nYour expenses equal $${expenses}. \nYour return on investment(ROI) is $${roi}.`)
}

console.log(winningsFunction())