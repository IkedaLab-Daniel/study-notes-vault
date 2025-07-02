import { useSelector } from "react-redux"
import { useActions } from "./use-actions";
import { increment, decrement, set } from "./action";

export const useCounter = () => {
    const count = useSelector(state => state.count);
    const actions = useActions({increment, decrement, set})

    return { count, ...actions}
}