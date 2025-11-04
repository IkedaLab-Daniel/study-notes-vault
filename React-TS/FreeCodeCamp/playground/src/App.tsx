import './App.css'

let name: string;
let age: number | string;
let isStudent: boolean;
let hobbies: string[] | boolean;
let role:[number|string, string];

type Person = {
  name: string;
  day?: number;
};

let person: Person = {
  name: "Ice",
  // day: 308,
};

let lotsIfPeople: Person[];

function App() {
  

  return (
    <>
      <p>Day 308 - LETSS GOOOOOOOOO!</p>
    </>
  )
}

export default App
