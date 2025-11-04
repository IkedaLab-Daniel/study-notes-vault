import './styles.css'

interface Props{
    todo: string;
    setToDo: React.Dispatch<React.SetStateAction<string>>;
}

const InputField: React.FC<Props> = ({todo, setToDo} : Props) => {

  return (
    <form className='input'>
        <input 
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
