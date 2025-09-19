import { useState, useDeferredValue } from "react";
import Slider from "./Slider";
import DisplayImage from "./DisplayImage";

export default function App() {
  const [blur, setBlur] = useState(0);
  const [brightness, setBrightness] = useState(100);
  const [contrast, setContrast] = useState(100);
  const [saturate, setSaturate] = useState(100);
  const [sepia, setSepia] = useState(0);

  const deferredBlur = useDeferredValue(blur);
  const deferredBrightness = useDeferredValue(brightness);
  const deferredContrast = useDeferredValue(contrast);
  const deferredSaturate = useDeferredValue(saturate);
  const deferredSepia = useDeferredValue(sepia);

  const filterStyle = `
  blur(${deferredBlur}px)
  brightness(${deferredBrightness}%)
  contrast(${deferredContrast}%)
  saturate(${deferredSaturate}%)
  sepia(${deferredSepia}%)`;

  return (
    <div className="app">
      <h1>Deferred Value</h1>
      <DisplayImage filterStyle={filterStyle} />
      <ul>
        <Slider
          value={blur}
          deferred={deferredBlur}
          onChange={(e) => setBlur(e.target.value)}
          name="Blur"
          max="20"
        />
        <Slider
          value={brightness}
          deferred={deferredBrightness}
          onChange={(e) => setBrightness(e.target.value)}
          name="Brightness"
          max="200"
        />
        <Slider
          value={contrast}
          deferred={deferredContrast}
          onChange={(e) => setContrast(e.target.value)}
          name="Contrast"
          max="200"
        />
        <Slider
          value={saturate}
          deferred={deferredSaturate}
          onChange={(e) => setSaturate(e.target.value)}
          name="Saturate"
          max="200"
        />
        <Slider
          value={sepia}
          deferred={deferredSepia}
          onChange={(e) => setSepia(e.target.value)}
          name="Sepia"
          max="100"
        />
      </ul>
    </div>
  );
}
