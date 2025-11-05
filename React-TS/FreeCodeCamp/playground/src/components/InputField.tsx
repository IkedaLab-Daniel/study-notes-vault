import { useRef } from 'react';
import './styles.css'

interface Props{
    todo: string;
    setToDo: React.Dispatch<React.SetStateAction<string>>;
    handleAdd: (e: React.FormEvent<HTMLFormElement>) => void;
}

const InputField: React.FC<Props> = ({todo, setToDo, handleAdd} : Props) => {

  const inputRef = useRef<HTMLInputElement>(null);

  return (
    <form className='input' onSubmit={(e) => {
        handleAdd(e);
        inputRef.current?.blur();
      }}>
        <input 
            ref={inputRef}
            type="text" 
            placeholder='Enter a task' 
            className='input__box'
            value={todo}
            onChange={(e) => setToDo(e.target.value)}
        />
        <button className='input_submit'>Go</button>
    </form>
  )
}

export default InputField
