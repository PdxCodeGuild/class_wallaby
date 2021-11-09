axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

window.addEventListener('DOMContentLoaded', (event) => {
    axios({
        method: 'get',
        url: "profilesniplist/" + (user_id),
        xstfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
            'X-CSRFToken': 'csrftoken',
        }
    }).then(response => {
        console.log(response.data)
        const subSnip = document.getElementById("submittedtasks")
        for (i = 0; i < response.data.length; i++) {
            const div = document.createElement("div");
            const button = document.createElement("button")
            div.innerHTML =
                `<div class='list-group mx-2'> 
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
                                <button class='profileSnip btn btn-danger row align-top' name= ${response.data[i].id} >Remove Snippet</button>
                            </div>
                        </div>
                    </div>
                </div>
            </br>`
            div.id = response.data[i].id
            subSnip.append(div);
        }
        const profileSnip = document.querySelectorAll('.profileSnip')
        for (let i = 0; i < profileSnip.length; i++) {
            profileSnip[i].addEventListener("click", function (event) {
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
                    console.log(response)
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
                    let parent = document.getElementById(event.target.name)
                    parent.remove()
                })
            })
        }
    })
})
window.addEventListener('DOMContentLoaded', (event) => {
    axios({
        method: 'get',
        url: "feedsubs/" + (user_id),
        xstfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
            'X-CSRFToken': 'csrftoken',
        }
    }).then(response => {
        console.log(response)
        let feedSubs = document.getElementById('feedSubscriptions')

        for (i = 0; i < response.data.AvailableFeeds.length; i++) {



            const div = document.createElement("div");
            div.innerHTML =

                `<div class='list-group mx-2'> 
                <div class='row align-items-start'> 
                        <div class = "d-flex w-100 justify-content-between">
                            <h5>${response.data.AvailableFeeds[i]}</h5> 
                        </div>
                       
                    </a>
                    <div class="row align-top">
                        <div class="col-4">
                            <button class='feedSnip btn btn-danger row align-top' name= "${response.data.AvailableFeeds[i]}" >Unsubscribe</button>
                        </div>
                    </div>
                </div>
            </div>
        </br>`
            div.id = response.data.AvailableFeeds[i]
            feedSubs.append(div)
        }
        const feedSnip = document.getElementsByClassName('feedSnip')
        for (i = 0; i < feedSnip.length; i++) {
            feedSnip[i].addEventListener('click', function (event) {


                axios({
                    method: 'get',
                    url: "feedsubs/" + (user_id),
                    xstfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                    headers: {
                        'X-CSRFToken': 'csrftoken',
                    }
                }).then(response => {
                    let feedName = event.target.name
                    let subs = response.data.AvailableFeeds
                    if (subs.includes(feedName) == true) {
                        const index = subs.indexOf(feedName)
                        console.log(subs)
                        if (index > -1) {
                            subs.splice(index, 1);
                            
                            axios({
                                method: 'patch',
                                url: "feedsubs/" + (user_id),
                                xstfCookieName: 'csrftoken',
                                xsrfHeaderName: 'X-CSRFToken',
                                data: {
                                    "AvailableFeeds": subs
                                },
                                headers: {
                                    'X-CSRFToken': 'csrftoken',
                                }
                            })
                            let parent = document.getElementById(feedName)
                            console.log(parent)
                            parent.remove()
                        }
                    }
                })
            })
        }
    })
})
