import { useDispatch, useSelector } from "react-redux";
import { set, increment, decrement } from "./action";

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
        </main>
    );
};

export default Counter;