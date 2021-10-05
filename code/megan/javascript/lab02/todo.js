// font
const body = document.querySelector()
body.style.fontFamily = 'sans-serif';

// incomplete task list
const add = document.querySelector('#btn-new-task')


const incomplete = document.querySelector('#incomplete-task-list')
console.log(incomplete)

function hideAndMove(event) {
    event.target.style.visibility = 'hidden'
        // move to completed list
}

incomplete.addEventListener('click', hideAndMove)

// remove task
const remove = document.querySelector('#btn-remove-task')
remove.addEventListener('click', function(event) {
    event.target.style.visibility = 'hidden'
})

const btn = document.querySelector('.btn')

// completed tasks
const completed = document.querySelector('#completed-tasks-list')
console.log(completed)

completed.style.textDecoration = 'line-through'

// button styling
btn.style.backgroundColor = 'blue'
btn.style.border = '1px dark-blue'
btn.style.color = 'white'