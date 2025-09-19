import { useState } from "react";
import Slider from "./Slider";
import DisplayImage from "./DisplayImage";

export default function App() {
  const [blur, setBlur] = useState(0);
  const [brightness, setBrightness] = useState(100);
  const [contrast, setContrast] = useState(100);
  const [saturate, setSaturate] = useState(100);
  const [sepia, setSepia] = useState(0);

  const filterStyle = `
    blur(${blur}px)
    brightness(${brightness}%)
    contrast(${contrast}%)
    saturate(${saturate}%)
    sepia(${sepia}%)
    `;

  return (
    <div className="app">
      <h1>Deferred Value</h1>
      <DisplayImage filterStyle={filterStyle} />
      <ul>
        <Slider
          value={blur}
          deferred={blur}
          onChange={(e) => setBlur(e.target.value)}
          name="Blur"
          max="20"
        />
        <Slider
          value={brightness}
          deferred={brightness}
          onChange={(e) => setBrightness(e.target.value)}
          name="Brightness"
          max="200"
        />
        <Slider
          value={contrast}
          deferred={contrast}
          onChange={(e) => setContrast(e.target.value)}
          name="Contrast"
          max="200"
        />
        <Slider
          value={saturate}
          deferred={saturate}
          onChange={(e) => setSaturate(e.target.value)}
          name="Saturate"
          max="200"
        />
        <Slider
          value={sepia}
          deferred={sepia}
          onChange={(e) => setSepia(e.target.value)}
          name="Sepia"
          max="100"
        />
      </ul>
    </div>
  );
}