console.log('hi')
const btn = document.getElementById("myBtn")
btn.addEventListener('click', getUrl)
let quote = document.getElementById('displayQuote').innerHTML

function getUrl() {
    fetch("https://favqs.com/api/qotd")
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data['quote']['body'])
            document.getElementById('displayQuote').innerHTML = data['quote']['body']         
        })
}
