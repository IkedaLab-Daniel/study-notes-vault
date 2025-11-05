import { useState } from 'react';
import './App.css'
import InputField from './components/InputField'
import type { Todo } from './model';

const App: React.FC = () => {
  const [todo, setToDo] = useState<string>("");
  const [todos, setToDos] = useState<Todo[]>([]);

  const handleAdd = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (todo){
      setToDos([...todos, {
        id: Date.now(),
        todo: todo,
        isDone: false
      }]);
      setToDo("");
    }

    console.log(todos)
  };

  console.log({todo});

  return (
    <div className='app'>
      <h2 className="heading">Taskify</h2>
      <InputField 
        todo={todo} 
        setToDo={setToDo} 
        handleAdd={handleAdd}
      />
      
      {todos.map((t) => (
        <li>{t.todo}</li>
      ))}

    </div>
  )
}

export default App
