import React, { useState } from 'react'
import type { Todo } from '../model'
import { AiFillDelete, AiFillEdit } from 'react-icons/ai'
import { MdDone } from 'react-icons/md'
import './styles.css'

type Props = {
    todo: Todo,
    todos: Todo[],
    setToDos: React.Dispatch<React.SetStateAction<Todo[]>>
}

const SingleTodo = ({todo, todos, setToDos}: Props) => {

  const [edit, setEdit] = useState<boolean>(false);
  const [editTodo, setEditToDo] = useState<string>(todo.todo);

  const handleDone = (id: number) => {
    setToDos(
        todos.map((todo) => 
            todo.id === id ? {...todo, isDone: !todo.isDone} : todo))
  };

   const handleDelete = (id: number) => {
    setToDos(todos.filter((todo)=>todo.id !== id));
  };

  const handleEdit = (e: React.FormEvent, id: number) => {
    e.preventDefault();
    setToDos(todos.map((todo) => (
        todo.id === id? {...todo, todo:editTodo} : todo
    )));
    setEdit(false);
  }


  return (
    <form className='todos__single' onSubmit={(e) => handleEdit(e, todo.id)}> 
        {
            edit ? (
                <input value={editTodo} onChange={(e) => setEditToDo(e.target.value)} className='todos__single--text' />
            ) : (
                todo.isDone ? (
                    <s className='todos__single--text'>{todo.todo}</s>
                ) : (
                    <span className='todos__single--text'>{todo.todo}</span>
                )
            )
        }


      <div>
        <span className="icon" onClick={() => {
            if (!edit && !todo.isDone) {
                setEdit(!edit);
            }
        }}>
            <AiFillEdit />
        </span>
        <span className="icon" onClick={() => handleDelete(todo.id)}>
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
