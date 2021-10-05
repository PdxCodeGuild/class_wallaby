
const text_field = document.getElementById("user_input");
const add = document.getElementById("add");
const remove = document.getElementById("remove");


add.addEventListener("click", function () {
    console.log(text_field.value);
  
    const li = document.createElement("li")
    li.innerHTML ="<li>" + text_field.value + "</li>"
    list.appendChild(li)
})

remove.addEventListener("click", function () {
    const li = document.querySelector("li")
    list.removeChild(li)
})

function hide(event) {
    event.target.style.textDecorationLine = "line-through";
    console.log(event.target, event.target.tagName);
  }
  const list = document.querySelector("#list");
  list.addEventListener("click", hide);