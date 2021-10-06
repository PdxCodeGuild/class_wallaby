// define variables
const textField = document.querySelector('#user-input')
const btnNew = document.querySelector('#btn-new-task')
const btnRemove = document.querySelector('#btn-remove-task')
const list = document.querySelector('#task-list')
const completed = document.querySelector('#completed-list')

// add item to list
btnNew.addEventListener('click', function() {
    let task = document.createElement('li');
    task.innerHTML = textField.value;
    list.appendChild(task);
});

// remove item from list
btnRemove.addEventListener('click', function(event) {
    // event.target.style.visibility = 'hidden';
    list.removeChild(event.target)
});

// mark item as completed
list.addEventListener('click', function(event) {
    completed.appendChild(event.target);
    completed.style.textDecoration = 'line-through';
});

// font
const body = document.querySelector('body')
body.style.fontFamily = 'sans-serif';

// button styling
const buttons = document.querySelector('.btn')
buttons.style.backgroundColor = 'blue'
buttons.style.border = '1px dark-blue'
buttons.style.color = 'white'

body.addEventListener('click', function(event) {
    if (event.target.className === 'btn') {
        let buttons = document.querySelector('.btn')
        buttons.style.backgroundColor = 'blue'
        buttons.style.border = '1px dark-blue'
        buttons.style.color = 'white'
    }
})