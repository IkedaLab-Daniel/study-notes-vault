//* Classes

//? Field types
class Car {
  static #nextSerialNumber: number
  static #generateSerialNumber() { return this.#nextSerialNumber++ }

  static {
    // `this` is the static scope
    fetch("https://api.example.com/vin_number_data")
        .then(response => response.json())
        .then(data => {
            this.#nextSerialNumber = data.mostRecentInvoiceId + 1;
        })
  }
  // serialNumber = Car.generateSerialNumber()

  static {}

  // private _serialNumber = Car.generateSerialNumber()
  #serialNumber = Car.#generateSerialNumber()
  protected get serialNumber() {
    return this.#serialNumber
  }

  constructor(
    make: string,
    model: string,
    year: number
  ) {}

  honk(duration: number): string {
    return `h${'o'.repeat(duration)}nk`
  }
  getLabel() {
  return `${this.make} ${this.model} ${this.year} - #${this.serialNumber}`
  }
}
Car.generateSerialNumber();
let sedan = new Car('Honda', 'Accord', 2017)
sedan.activateTurnSignal("left") //! not safe!
new Car(2017, "Honda", "Accord") //! not safe!


//? method types
const c = new Car("Honda", "Accord", 2017);
c.honk(5); // "hooooonk"


//? static member fields

console.log( new Car("Honda", "Accord", 2017))
// > "Honda Accord 2017 - #100
console.log( new Car("Toyota", "Camry", 2022))
// > "Toyota Camry 2022 - #101


//? static blocks

//* Access modifier keywords
  // const s = new Sedan("Nissan", "Altima", 2020)
  // s.serialNumber
//? on member fields
Car.generateSerialNumber()

//? on static fields

//* JS private #fields

//? member fields
c.#serialNumber


//? static fields
#serialNumber = Car.#generateSerialNumber()

//* Private field presence checks

// equals(other: unknown) {
//     if (other &&
//       typeof other === 'object' &&
//       #serialNumber in other) {
//         other
// //       ^?
//         return other.#serialNumber = this.#serialNumber
//       }
//       return false
//   }
// const c2 = c1
// c2.equals(c1)

// readonly

// readonly #serialNumber = Car.#generateSerialNumber()
// changeSerialNumber(num: number) {
//     this.#serialNumber = num
// }

// * Parameter properties

class Base {}

class Car2 extends Base {
  foo = console.log("class field initializer")
  constructor(public make: string) {
    super()
    console.log("custom constructor stuff")
  }
}

//* Overrides

class Truck extends Car {
    override honk(duration: number) { // OOPS!
        return ("BEEP")
    }
}

const t = new Truck("Ford", "F-150", 2020);
t.honk(5); // "beep"

//? override keyword
// override hoonk() { // OOPS!

//? noImplicitOverride
// "noImplicitOverride": true

/**/
export default {}
