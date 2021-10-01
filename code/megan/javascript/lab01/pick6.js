function pick6() {

    let ticket = [];
    let min = 1;
    let max = 99;

    function getRandomInt(min, max) {
        // let min = Math.ceil(1);
        // let max = Math.floor(99);
        console.log(Math.floor(Math.random() * (max - min)))
        return Math.floor(Math.random() * (max - min))
    };

    for (let i = 0; i < 7; i++) {
        ticket.push(getRandomInt(min, max));
    }

    return ticket
}

const winningTicket = pick6()
console.log(winningTicket)

function compareMatches(winning, ticket) {
    console.log(winning, ticket)

    let matches = 0;

    for (let i = 0; i < winning.length; i++) {
        if (winning[i] === ticket[i])
            matches += 1;
    }

    return matches
}

function winningsFunction() {

    const winningsObject = {
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    }

    let balance = 0;
    let expenses = 0;
    let earnings = 0;
    let roi = 0;

    // let indicators = {
    //     balance: 0,
    //     expenses: 0,
    //     earnings: 0,
    //     roi: 0,
    // }

    for (let i = 0; i < 3; i++) {
        balance -= 2;
        expenses += 2;
        earnings += (winningsObject[compareMatches(winningTicket, pick6())]);
        roi += ((earnings - expenses) / expenses);
    }

    // let roi = earnings - expenses / expenses;

    let indicators = [
        balance[i],
        expenses[i],
        earnings[i],
        roi[i],
    ]

    console.log(`After 100,000 tries, your balance is $${balance}. \nEarnings: $${earnings} \nExpenses: $${expenses} \nReturn on investment(ROI): $${roi}`)
    alert(`After 100,000 tries, your balance is $${balance}. \nEarnings: $${earnings} \nExpenses: $${expenses} \nReturn on investment(ROI): $${roi}`)

    return indicators
}

winningsFunction()