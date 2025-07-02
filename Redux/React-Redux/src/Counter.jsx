import { SetCounter } from "./SetCounter";
import { useCounter } from "./use-counter";

export const Counter = () => {
    const incident = 'Incident';
    const { count, increment, decrement, set } = useCounter()


    return (
        <main className="Counter">
            <h1>Counter</h1>
            <p className="count">{count}</p>
                <section className="controls">
                    <button onClick={() => increment()}>Increment</button>
                    <button onClick={() => set(0)}>Reset</button>
                    <button onClick={() => decrement()}>Decrement</button>
                </section>
                <SetCounter 
                    onSubmit = {value => dispatch(set(value))}
                />
        </main>
    );
};

export default Counter;