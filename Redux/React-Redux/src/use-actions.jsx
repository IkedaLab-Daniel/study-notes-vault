import { useDispatch } from "react-redux"
import { bindActionCreators} from 'redux'

export const useActions = (actions) => {
    const dispatch = useDispatch();
    return bindActionCreators(actions, dispatch)
}