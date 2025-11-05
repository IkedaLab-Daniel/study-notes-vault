import React from 'react'
import type { Todo } from '../model'
import { AiFillDelete, AiFillEdit } from 'react-icons/ai'
import { MdDone } from 'react-icons/md'
import './styles.css'
import ToDoList from './ToDoList'

type Props = {
    todo: Todo,
    todos: Todo[],
    setToDos: React.Dispatch<React.SetStateAction<Todo[]>>
}

const SingleTodo = ({todo, todos, setToDos}: Props) => {

  const handleDone = (id: number) => {
    setToDos(
        todos.map((todo) => 
            todo.id === id ? {...todo, isDone: !todo.isDone} : todo))
  }

  return (
    <form className='todos__single'>
        {
            todo.isDone ? (
                <s className='todos__single--text'>{todo.todo}</s>
            ) : (
                <span className='todos__single--text'>{todo.todo}</span>
            )
        }

      <div>
        <span className="icon">
            <AiFillEdit />
        </span>
        <span className="icon">
            <AiFillDelete />
        </span>
        <span className="icon" onClick={() => handleDone(todo.id)}>
            <MdDone />
        </span>
      </div>
    </form>
  )
}

export default SingleTodo
