const input = document.getElementById('todoInput')
const addBtn = document.getElementById('todoAdd')
const deleteBtn = document.getElementById('todoDelete')
const incompLi = document.getElementById('incompleteList')
const compLi = document.getElementById('completeList')

const addTodo = e => {
  const newTodo = document.createElement('li')
  newTodo.innerText = input.value
  incompLi.appendChild(newTodo)
}

const markComplete = e => {
  incompLi.removeChild(e.target)
  const newChild = compLi.appendChild(e.target)
  console.dir(newChild.style.textDecoration = 'line-through')
}

addBtn.addEventListener('click', addTodo)
incompLi.addEventListener('click', markComplete)