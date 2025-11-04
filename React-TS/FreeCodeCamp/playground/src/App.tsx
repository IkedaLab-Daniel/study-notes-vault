import './App.css'

let name: any;
let age: number | string;
let isStudent: boolean;
let hobbies: string[] | boolean;
let role:[number|string, string];

let printName: (name:string) => void;
let sum: (x:number, y:number) => number | string;
let neva: () => never;

// function printName(name: string) {
//   console.log(name)
// };
// printName('Ice');


// type Person = {
//   name: string;
//   day?: number;
// };

let person: Person = {
  name: "Ice",
  // day: 308,
};

let lotsIfPeople: Person[];

let personName: unknown;

// type X = {
//   a: string;
//   b: number;
// };

// type Y = X & {
//   c: string;
//   d: number;
// };

// let y : Y = {
//   c: "Ice",
//   d: 308,
// }

interface Person {
  name: string;
  age?: number;
};

interface Guy extends Person {
  profession: string;
};

function App() {
  

  return (
    <>
      <p>Day 308 - LETSS GOOOOOOOOO!</p>
    </>
  )
}

export default App
