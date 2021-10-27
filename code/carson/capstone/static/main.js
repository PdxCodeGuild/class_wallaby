console.log('hello worl');
const remove = document.getElementById("remove");
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

remove.addEventListener("click", function () {
    const li = document.querySelector("li")
    list.removeChild(li)
})

