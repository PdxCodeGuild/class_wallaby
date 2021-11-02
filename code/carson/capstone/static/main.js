
const date = document.querySelector(".fatsecret_servingentry_date_input")
const meal = document.querySelector(".fatsecret_servingentry_meal_input")
const name = document.querySelector(".fatsecret_servingentry_name_input")
const amount = document.querySelector(".fatsecret_servingentry_amount_input")
const save = document.querySelectorAll('.fatsecrect_button')

// if (save){
//     console.log(save)
// 

console.log(date)


const navSlide = () => {
    const burger = document.querySelector('.burger')
    const nav = document.querySelector('.nav-links')
    const navLinks = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click', () => {
        //Toggle NAv   
        nav.classList.toggle('nav-active');
        //Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 1}s `;
                console.log(index / 7)
            }
        });
        //Burger Animation
        burger.classList.toggle('toggle');

    });
}

navSlide();

// remove.addEventListener("click", function () {
//     const li = document.querySelector("li")
//     list.removeChild(li)
// })
















// const info = {
//     name: '===> Grab this from the HTML'
//     meal: '===> Grab this from the HTML'

// }    

// function PostInfo(){
//     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//     fetch('http://127.0.0.1:8000/api/info/', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json',
//         'X-CSRFToken': csrftoken,
//     },
//     body: JSON.stringify(info),
// })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Success:', data);
//     })
//     .catch((error) => {
//         console.error('Error:', error);
//     });
// }