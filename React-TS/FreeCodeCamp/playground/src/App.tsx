import './App.css'

let name: string;
let age: number | string;
let isStudent: boolean;
let hobbies: string[] | boolean;
let role:[number|string, string];

let printName: (name:string) => void;
let sum: (x:number, y:number) => number | string;

// function printName(name: string) {
//   console.log(name)
// };
// printName('Ice');

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
