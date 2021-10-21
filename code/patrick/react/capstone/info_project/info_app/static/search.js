axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';



window.addEventListener('DOMContentLoaded', (event) => {
    let params = new URLSearchParams(document.location.search.substring(1));
    let qstring = params.get("q"); // is the string for the query
    // document.getElementById("mySearch").value = qstring;

    let url1 = 'api/?q='
    let x = url1 + qstring
    console.log(x)
    axios({
        method: 'get',
        url: x,
        xstfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
            'X-CSRFToken': 'csrftoken',
        }
    }).then(response => {
        console.log(response.data[1].subscriber)
        const deleteBtn = document.getElementById('deleteSub')
        for (i = 0; i < response.data.length; i++) {
            if (response.data[i].subscriber.includes(user_id)) {
                console.log(response.data[i].id, 'subscribed')
                const div = document.createElement("div");
                div.innerHTML =
                    `
                <div class='list-group mx-2'> 
                    <div class='row align-items-start'> 
                        <a href = ${response.data[i].link} class='list-group-item list-group-item-action'> 
                            <div class = "d-flex w-100 justify-content-between">
                                <h5>${response.data[i].title}</h5> 
                            </div>
                            <p class='mb-1'>Published on: <bold> ${response.data[i].pubDate} </bold></p>
                            <small>Description:  <bold> ${response.data[i].description} </bold></small>
                        </a>
                        <div class="row align-top">
                            <div class="col-4">
                                <button class='btnSnip btn btn-primary row align-top btn-success' name= ${response.data[i].id} >Added</button>
                            </div>
                        </div>
                    </div>
                </div>
            </br>`
                div.id = response.data[i].id
                deleteBtn.append(div)
            }
            else {
                const div = document.createElement("div");
                div.innerHTML =
                    `
                <div class='list-group mx-2'> 
                    <div class='row align-items-start'> 
                        <a href = ${response.data[i].link} class='list-group-item list-group-item-action'> 
                            <div class = "d-flex w-100 justify-content-between">
                                <h5>${response.data[i].title}</h5> 
                            </div>
                            <p class='mb-1'>Published on: <bold> ${response.data[i].pubDate} </bold></p>
                            <small>Description:  <bold> ${response.data[i].description} </bold></small>
                        </a>
                        <div class="row align-top">
                            <div class="col-4">
                                <button class='btnSnip btn btn-primary row align-top' name= ${response.data[i].id} >Add Snippet</button>
                            </div>
                        </div>
                    </div>
                </div>
            </br>`
                div.id = response.data[i].id
                deleteBtn.append(div)
            }
        }
        const btnSnip = document.querySelectorAll('.btnSnip');
        for (let i = 0; i < btnSnip.length; i++) {
            btnSnip[i].addEventListener("click", function (event) {

                let classes = event.target.classList
                let result = classes.toggle("btn-success");
                if (result) {
                    btnSnip.textContent = `'btn-success' removed; classList is now "${classes}".`;
                    event.target.innerText = 'Added'

                    let snipId = event.target.name
                    axios({
                        method: 'get',
                        url: "snipsubs/" + (snipId),
                        xstfCookieName: 'csrftoken',
                        xsrfHeaderName: 'X-CSRFToken',
                        headers: {
                            'X-CSRFToken': 'csrftoken',
                        }
                    }).then(response => {
                        let snipId = response.data.id
                        let subs = response.data.subscriber
                        console.log(snipId)
                        if (subs.includes(user_id) == true) {
                            alert('already added this snippet')
                        }
                        else {
                            console.log('add subs')
                            axios({
                                method: 'patch',
                                url: "snipsubs/" + (snipId),
                                xstfCookieName: 'csrftoken',
                                xsrfHeaderName: 'X-CSRFToken',
                                data: {
                                    "subscriber": [user_id]
                                },
                                headers: {
                                    'X-CSRFToken': 'csrftoken',
                                }
                            })
                        }
                    })
                }
                else {
                    btnSnip.textContent = `'btn-success' added; classList is now "${classes}".`;
                    event.target.innerText = 'Add Snippet'
                    console.log('remove subs')


                    let snipId = event.target.name
                    console.log(snipId)
                    axios({
                        method: 'get',
                        url: "snipsubs/" + (snipId),
                        xstfCookieName: 'csrftoken',
                        xsrfHeaderName: 'X-CSRFToken',
                        headers: {
                            'X-CSRFToken': 'csrftoken',
                        }
                    }).then(response => {
                        let snipId = response.data.id
                        let subs = response.data.subscriber

                        if (subs.includes(user_id) == true) {
                            const index = subs.indexOf(user_id)
                            if (index > -1) {
                                subs.splice(index, 1);
                            }
                        }
                        axios({
                            method: 'patch',
                            url: "snipsubs/" + (snipId),
                            xstfCookieName: 'csrftoken',
                            xsrfHeaderName: 'X-CSRFToken',
                            data: {
                                "subscriber": subs
                            },
                            headers: {
                                'X-CSRFToken': 'csrftoken',
                            }
                        })
                    })

                }
            })
        }


    })
});


