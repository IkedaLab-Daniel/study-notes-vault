import React from 'react'
import './styles.css'
import type { Todo } from '../model'
import SingleTodo from './SingleTodo';

interface Props {
    todos: Todo[];
    setToDos: React.Dispatch<React.SetStateAction<Todo[]>>;    
};

const ToDoList: React.FC<Props> = ({todos, setToDos}) => {
  return (
    <div className='todos'>
      {todos.map((todo) => (
        <SingleTodo 
            todo={todo} 
            key={todo.id} 
            todos={todos}
            setToDos={setToDos}
        />
      ))}
    </div>
  )
}

export default ToDoList
