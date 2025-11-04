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


interface Person {
  name: string;
  age?: number;
};

type X = {
  a: string;
  b: number;
};

// type X = Person & {
//   a: string;
//   b: number;
// };

// interface Person extends X {
//   name: string;
//   age?: number;
// };

function App() {
  

  return (
    <>
      <p>Day 308 - LETSS GOOOOOOOOO!</p>
    </>
  )
}

export default App
