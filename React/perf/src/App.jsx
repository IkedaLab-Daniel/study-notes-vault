import { useEffect, useState } from "react";
import { marked } from "marked";

import MarkdownPreview from "./MarkdownPreview";
import markdownContent from "./markdownContent";

export default function App() {
  const [text, setText] = useState(markdownContent);
  const [time, setTime] = useState(Date.now())
  const [theme, setTheme] = useState("blue")

  useEffect(() => {
    const interval = setInterval(() => {
      setTime(Date.now())
    }, 1000)
  }, [])

  const options = { text, theme }
  const render = (text) => marked.parse(text);
}