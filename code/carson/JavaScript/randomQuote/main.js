const info = document.getElementById('quote')
const search = document.getElementById("search");
const btn = document.getElementById("btn");
const key = new Headers();


// key.append('Authorization', 'Token token=" edda3616a59950596dbacd4038e5980e  "');

// fetch('https://favqs.com/api/quotes/?filter=funny&type=tag'), {
//     method: 'GET',
//     headers: key,
// }

//     .then(res => res.json())
//     .then(data => {
//         console.log(data)
//         let quote = data.quote.body
//         console.log(quote)
//         info.innerHTML = quote

//     })
//     .catch(function (error) {
//         console.error('There has been a problem with your fetch operation:', error);
//     });

btn.addEventListener("click", function () {
    console.log(search.value);


})