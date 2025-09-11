import { hydrateRoot } from "react-dom/client"
import { createElement as h } from "react"
import App from "./app.js"

hydrateRoot(document.getElementById("root"), h(App));
