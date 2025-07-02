import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { set } from "./action";

export const SetCounter = ({ onSubmit }) => {
  const countFromStore = useSelector(state => state.count);
  const [count, setCount] = useState(countFromStore) ;
  const dispatch = useDispatch();

  useEffect(()=>{
    setCount(countFromStore)
  }, [countFromStore]);

  return (
    <section>
      <form
        onSubmit={(event) => {
          event.preventDefault();
          dispatch(set(count))
        }}
      >
        <label htmlFor="set-to">Set Count</label>
        <input 
            id="set-to" 
            type="number"
            value = {count}
            onChange={(e) => setCount(e.target.value)}
         />
        <input type="submit" />
      </form>
    </section>
  );
};