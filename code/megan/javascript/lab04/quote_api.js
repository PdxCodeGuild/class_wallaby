const myHeaders = new Headers();

myHeaders.append('Authorization', 'Token token="  PASTE YOUR API KEY  "');

fetch(url, {
        method: 'GET',
        headers: myHeaders,
    })
    .then(function(response) {
        return response.json()
    })
    .then(function(data) {
        //or pass a callback function to handle data
        console.log(data)
    })
    .catch(function(error) {
        console.error('There has been a problem with your fetch operation:', error);
    });