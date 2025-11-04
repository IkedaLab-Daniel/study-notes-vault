import React from 'react'
import './styles.css'

const InputField = () => {
  return (
    <form className='input'>
        <input type="text" placeholder='Enter a task' className='input__box'/>
        <button className='input_submit'>Go</button>
    </form>
  )
}

export default InputField
