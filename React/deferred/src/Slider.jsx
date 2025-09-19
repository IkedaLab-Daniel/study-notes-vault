export default function Slider({ value, deferred, onChange, name, max }) {
  return (
    <li className="slider">
      <label htmlFor={name}>
        {name}
        {value !== deferred ? " (Updating)" : ""}
      </label>
      <input
        type="range"
        id={name}
        name={name}
        min="0"
        max={max}
        value={value}
        onChange={onChange}
      />
      <output htmlFor={name}>
        Actual Value: {value} | Deferred Value: {deferred}
      </output>
    </li>
  );
}
