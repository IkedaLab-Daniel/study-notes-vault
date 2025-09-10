import { createElement as h, useState } from "react";

function App(){
    const [count, setCount] = useState()
    return h(
        "div",
        null,
        h("h1", null, "Hello Frontend Masters"),
        h("p", null, "this is ssr"),
        h("button", {onClick: () => setCount(count + 1) }, `Count: ${count}`)
    )
}

export default App