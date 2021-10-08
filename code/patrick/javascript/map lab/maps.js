const btn = document.getElementById("myBtn")
btn.addEventListener('click', getRandom)
let cords=[]

async function getRandom() {
    let apiReturn = await axios.get('http://api.geonames.org/citiesJSON?north=44.1&south=-9.9&east=-22.4&west=55.2&lang=de&username=pbpdx');
    let data = apiReturn.data.geonames;
    // console.log(typeof data)
    // console.log(data)
    for (i = 0; i < 9; i++) {
        let x = (data[i]['lat'])
        let y = (data[i]['lng'])
        cords.push({x, y})
        L.marker([x, y]).addTo(mymap);
    }
    // console.log(coordinates)
   }

console.log(cords)
let mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoicGJwZHgiLCJhIjoiY2t1ZGl5bGx6MDBiYjJ2dDlsZTZ3YjJxdCJ9.Fqn9wR46Fz2Bg4QP79TB8g'
}).addTo(mymap);



