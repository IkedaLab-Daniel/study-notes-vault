import { useState, useEffect, useMemo, useCallback } from "react";
import { marked } from "marked";

import MarkdownPreview from "./MarkdownPreview";
import markdownContent from "./markdownContent";

export default function App() {
  const [text, setText] = useState(markdownContent);
  const [time, setTime] = useState(Date.now());
  const [theme, setTheme] = useState("green");

  useEffect(() => {
    const interval = setInterval(() => {
      setTime(Date.now());
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const render = useCallback((text) => marked.parse(text), []);
  const options = useMemo(() => ({ text, theme }), [text, theme]);

  return (
    <div className="app">
      <h1>Performance with React</h1>
      <h2>Current Time: {time}</h2>
      <label htmlFor={"theme"}>
        Choose a theme:
        <select value={theme} onChange={(e) => setTheme(e.target.value)}>
          <option value="green">Green</option>
          <option value="blue">Blue</option>
          <option value="red">Red</option>
          <option value="yellow">Yellow</option>
        </select>
      </label>
      <div className="markdown">
        <textarea
          className="markdown-editor"
          value={text}
          onChange={(e) => setText(e.target.value)}
        ></textarea>
        <MarkdownPreview options={options} render={render} />
      </div>
    </div>
  );
}