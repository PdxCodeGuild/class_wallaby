axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// axios({
//     method: 'get',
//     url: "https://www.federalregister.gov/api/v1/agencies",
//     xstfCookieName: 'csrftoken',
//     xsrfHeaderName: 'X-CSRFToken',
//     headers: {
//         'X-CSRFToken': 'csrftoken',
//     }
// }).then(response => {
//     console.log(response)
// })