import { useDispatch, useSelector } from "react-redux";
import { set, increment, decrement } from "./action";
import { SetCounter } from "./SetCounter";
export const Counter = () => {
    const incident = 'Incident';
    const count = useSelector(state => state.count);
    const dispatch = useDispatch();


    return (
        <main className="Counter">
            <h1>Counter</h1>
            <p className="count">{count}</p>
                <section className="controls">
                    <button onClick={() => dispatch(increment())}>Increment</button>
                    <button onClick={() => dispatch(set(0))}>Reset</button>
                    <button onClick={() => dispatch(decrement())}>Decrement</button>
                </section>
                <SetCounter 
                    onSubmit = {value => dispatch(set(value))}

                />
        </main>
    );
};

export default Counter;