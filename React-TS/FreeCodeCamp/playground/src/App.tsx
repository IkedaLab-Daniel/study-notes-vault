import { useState } from 'react';
import './App.css'
import InputField from './components/InputField'

const App: React.FC = () => {
  const [todo, setToDo] = useState<string>("");

  console.log({todo});

  return (
    <div className='app'>
      <h2 className="heading">Taskify</h2>
      <InputField todo={todo} setToDo={setToDo} />
    </div>
  )
}

export default App
