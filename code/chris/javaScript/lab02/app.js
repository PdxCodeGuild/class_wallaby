const input = document.getElementById('todoInput')
const addBtn = document.getElementById('todoAdd')
const deleteBtn = document.getElementById('todoDelete')
const incompLi = document.getElementById('incompleteList')
const compLi = document.getElementById('completeList')

const addTodo = e => {
  if (input.value) {
    const newTodo = document.createElement('li')
    newTodo.className = 'todo'
    newTodo.innerText = input.value
    input.value = ''
    incompLi.appendChild(newTodo)

  }
}

const deleteTodo = e => {
  const todosArray = document.getElementsByClassName('todo')
  for (const todo of todosArray) {
    if (todo.innerText === input.value){
      todo.parentNode.removeChild(todo)
    }
  }
  input.value = ''
}

const markComplete = e => {
  incompLi.removeChild(e.target)
  const newChild = compLi.appendChild(e.target)
  console.dir(newChild.style.textDecoration = 'line-through')
}

addBtn.addEventListener('click', addTodo)
incompLi.addEventListener('click', markComplete)
deleteBtn.addEventListener('click', deleteTodo)