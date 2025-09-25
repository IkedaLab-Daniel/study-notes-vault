# TypeScript 5+ Fundamentals, v4
[TypeScript 5+ Fundamentals, v4 – Introduction (Frontend Masters)](https://frontendmasters.com/courses/typescript-v4/introduction/)

## Course Introduction & Key Takeaways

- **Instructor:** Mike North, Principal Staff Engineer at Stripe, tech lead for Stripe's external developer platform (Node.js SDK, Stripe Workbench, public API design).
- **TypeScript at Stripe:** Used for shaping high-stakes APIs, ensuring correct request/response shapes, and powering large-scale payment systems.
- **Course Goal:** Build a strong mental model for how TypeScript works, not just feature memorization. Focus on understanding types and how to model data.

### What is TypeScript?
- Open source, maintained by Microsoft.
- Syntactic superset of JavaScript: all JS syntax works in TS, but not all JS programs are valid TS.
- Three parts: the language, the compiler (outputs clean JS), and the language server (powers IDE features like autocomplete and inline errors).
- TypeScript acts like a powerful linter: it only checks types at build time, then compiles away to regular JavaScript for runtime.
- No runtime type validation (unlike Java or C#); all type checking is at build time.
- TypeScript is extremely popular and is now a standard part of modern frontend stacks.

### Why Use Types?
- Types let you express intent in code, making it clear how functions and data should be used.
- TypeScript catches errors at compile time, not runtime, providing faster and clearer feedback.
- Types help document code, making it easier to understand and maintain, especially in large or complex codebases.
- Example: Typing a function makes its intended use clear and prevents bugs from mixed types (e.g., adding numbers vs. concatenating strings).
- TypeScript is not a replacement for unit tests, but it provides immediate feedback and helps catch many issues early.

### Course Structure & Topics
- Build a small TypeScript program using the CLI.
- Cover variables, values, object, array, and tuple types.
- Discuss structural vs. nominal type systems.
- Explore union and intersection types (TypeScript's "and/or" for types).
- Learn about interfaces, type aliases, and naming types for reuse across modules.
- Exercise: Write a type for any valid JSON value.
- Type queries: Extract types from values (e.g., function return types).
- Callables and constructables: Functions vs. classes.
- Type guards and narrowing: Handling specific parts of types in code branches.
- Generics: Parameterize types for flexible, reusable code.
- Final project: Build map, filter, and reduce utilities for dictionaries (not just arrays).

### Pros & Cons of TypeScript Strictness
- Strict typing moves errors from runtime to compile time, making bugs easier to catch and fix.
- Dynamic typing (JavaScript) is flexible but can lead to subtle bugs that are only caught at runtime.
- TypeScript helps encode conventions and constraints in code, making large and complex projects more maintainable.
- You can still introduce flexibility in TypeScript using advanced type features (covered later in the course).

## Environment Setup & Tooling

- **Course website:** [typescript-training.com](https://typescript-training.com) (for code snippets and exercises)
- **Official docs:** [typescriptlang.org](https://typescriptlang.org)
- **Hands-on learning is encouraged**—best way to learn TypeScript is by coding along.
- **Volta** is recommended for managing Node and Yarn versions:
  - Install with: `curl https://get.volta.sh | bash`
  - Close and reopen your terminal after install (updates shell config)
  - Use Volta to globally install Node 18 LTS and Yarn v3: `volta install node@18 yarn@3`
  - Ensures consistent environment for the course
  - Alternatives: nvm, N, or Windows MSI installer (see Volta docs)
- **Cloning the course repo:**
  - Use HTTPS to clone (no need for SSH keys)
  - Run `yarn` in the project folder to install dependencies
  - Look for output starting with `Y` (indicates Yarn 3+)
  - Yarn 1 is deprecated; use Yarn 3 or 4 (release candidate is fine)
  - Node and Yarn versions are pinned in the root `package.json` (Node 18.18.2, Yarn 3.6.4)

## Variables, Values, and Type Inference

- The course uses the `notes-ts-fundamentals-v4` package for hands-on TypeScript examples, matching the website’s code snippets.
- **Variable Declarations:**
  - `let` allows reassignment; TypeScript infers the type from the initial value (e.g., `let temperature = 6` infers `number`).
  - TypeScript enforces that a variable’s type cannot change after initialization.
  - `const` creates an immutable binding; the value cannot be reassigned. For primitive values (like numbers), the value itself is immutable.
- **Literal Types:**
  - With `const humidity = 79`, TypeScript infers the type as the literal `79` (not just `number`).
  - Literal types represent a set with only one allowed value (e.g., only `79`).
  - Assigning a general type (like `number`) to a literal type (like `79`) is not allowed, but the reverse is fine.
  - Casting (e.g., `let humidity = 10 as 79`) is possible but not recommended, as it overrides TypeScript’s safety.
- **Type as Sets:**
  - Think of types as sets of allowed values. `number` is the set of all numbers; a literal type like `79` is a set with one value.
- **Type Annotations:**
  - If a variable is declared without initialization (e.g., `let endTime;`), TypeScript infers `any` (implicit any), which is not ideal.
  - Use type annotations (e.g., `let endTime: Date;`) to specify the intended type and avoid losing type information.
  - Type annotations work for variables, function parameters, return types, and class fields.
- **Best Practices:**
  - Prefer explicit type annotations when TypeScript cannot infer the type.
  - Avoid using `any` unless necessary, as it removes type safety.
  - Use `const` for values that should not change, and let TypeScript infer literal types when appropriate.

## TypeScript Function Typing and Linting

* Adding explicit types (`a: number, b: number, : number`) makes TypeScript stricter and prevents hidden `any` values.
* Without types, TypeScript may infer `any`, allowing bugs (e.g., passing `add(1,2)` directly to a `Promise` constructor).
* Explicit return types act as a **contract**:

  * Prevents sneaky bugs (e.g., function returning `number | undefined`).
  * Errors show up at the function definition, not scattered across all call sites.
* Type inference works, but explicit types make intent clear and errors closer to the source.
* ESLint is still useful with TypeScript:

  * TypeScript = type checking (low-level).
  * ESLint = code style, best practices (high-level).
  * `typescript-eslint` allows ESLint to leverage type info for powerful rules.
* Explicit return types are recommended for production code, especially when functions are reused across modules.

## Objects: Excess property check
* **TypeScript’s “excess property check” only runs for object *literals* assigned directly to a typed target.**
* If you spread a value or pass a variable, the compiler won’t do that simple literal check (because the object is being composed and its exact keys aren’t known at compile time).
* For real APIs you should *also* do runtime validation (TS is compile-time only).

Below are concrete examples, why this happens, and practical patterns you can use.

---

### 1) The excess-property error (object literal)

```ts
interface Car {
  make: string;
  model: string;
  year: number;
  chargingVoltage?: number;
}

function printCar(c: Car) {
  console.log(c.make);
}

printCar({
  make: "Ford",
  model: "F-150",
  year: 2020,
  color: "red", // <-- TS Error: 'color' does not exist on type 'Car'
});
```

TypeScript complains because you passed an object literal with a key (`color`) that `Car` does not declare. This is a helpful guard against typos and accidental extra props.

---

### 2) Spread or variable bypasses that check

```ts
const extra = { color: "red" };
printCar({ make: "Ford", model: "F-150", year: 2020, ...extra }); // no compile error
```

When you spread/compose or pass a variable, TS stops doing the simple literal excess check — it assumes you intentionally composed the object.

---

### 3) How to *enforce* “no extra props” at compile time (patterns)

**A. Pick only known props (safe and explicit):**

```ts
const raw = { make: "Ford", model: "F-150", year: 2020, color: "red" };
const { make, model, year, chargingVoltage } = raw;
printCar({ make, model, year, chargingVoltage }); // safe — unknown keys excluded
```

**B. Small helper to fail on extras (compile-time trick):**

```ts
// If you really want a compile-time error for extras:
function assertNoExtra<T>(obj: T & Record<Exclude<string, keyof T>, never>) {
  return obj;
}

const car = assertNoExtra<Car>({
  make: "Ford",
  model: "F-150",
  year: 2020,
  color: "red", // <-- compile error: 'color' is excess
});
```

That `assertNoExtra` pattern is a bit of a TypeScript trick. It’s useful in libraries/tests when you want strictness, but it’s not commonly used everywhere.

---

### 4) Runtime enforcement — **do this for APIs**

TypeScript is compile-time only. For data coming from clients (req.body), always validate at runtime and **strip** unknown keys. I recommend schema validators like **Zod** or **Joi**:

```ts
import { z } from "zod";

const CarSchema = z.object({
  make: z.string(),
  model: z.string(),
  year: z.number(),
  chargingVoltage: z.number().optional(),
}).strict(); // `.strict()` rejects unknown keys

// in your handler
const parsed = CarSchema.parse(req.body); // throws if unknown/invalid
printCar(parsed);
```

`z.object(...).strict()` will either throw or let you `.safeParse()` and return errors — this is how you *prevent* stray properties at runtime (and return good error messages to clients).

---

### 5) Practical recommendations

* For params coming from clients: **always** validate and sanitize at runtime (Zod/Joi/Yup). Don’t rely on TS for this.
* For internal object composition (in code): prefer destructuring or building explicit DTO objects rather than blindly spreading external objects.
* If you absolutely need compile-time “exactness” for literals, use `assertNoExtra<T>(...)` or similar helper in the places where it matters (tests, library boundaries).
* Use TS types for developer ergonomics, and schema validators for correctness at runtime.

### 🔑 What’s an Index Signature?

An **index signature** tells TypeScript:

> “This object can have properties with arbitrary keys of a certain type, and their values must follow a certain type.”

Syntax:

```ts
type PhoneNumbers = {
  [key: string]: string; // any string key → must map to a string value
};
```

That means:

```ts
const phones: PhoneNumbers = {
  home: "123-456-7890",
  work: "987-654-3210",
  customLabel: "555-555-5555", // allowed, even if not predefined
};
```

✅ Works with *any* string key
❌ But values must be strings (numbers or other types won’t compile).

---

### 📓 Dictionary Use Case

An index signature is like a **dictionary / hash map** in other languages.
For example:

```ts
type CurrencyAmounts = {
  [currencyCode: string]: number;
};

const balances: CurrencyAmounts = {
  USD: 100,
  JPY: 5000,
  EUR: 80,
};
```

This is great for:

* Arbitrary keys from an external source (like API JSON).
* Cases where ordering doesn’t matter (unlike arrays).

---

### 🛠️ Mixing Known Properties + Index Signature

You can **combine fixed properties** (guaranteed fields) with flexible keys:

```ts
type Phones = {
  mobile: string;             // always required
  [key: string]: string;      // allow any other phone labels
};

const phones: Phones = {
  mobile: "123-456-7890",
  home: "111-111-1111",
  fax: "222-222-2222",
  custom1: "333-333-3333",
};
```

Here:

* `phones.mobile` is guaranteed.
* `phones["home"]` or `phones["randomLabel"]` is allowed, but may not exist.

---

### 📍 Dot Notation vs Bracket Notation

* **Dot notation** → use for *known properties* (`phones.mobile`).
* **Bracket notation** → use for *dictionary-style keys* (`phones["home"]`).

This makes code clearer, and TS compiler options (`noUncheckedIndexedAccess`) can enforce safety:

```ts
phones["random"] // type: string | undefined (safer)
```

---

### ❓ Why not always use arrays?

* Arrays imply **order** → doesn’t matter for “label → value” mappings.
* Objects with index signatures better represent **key-value lookups**.

Example from Stripe API:

```ts
// Instead of array of {currency, amount}
{
  USD: 1000,
  JPY: 50000
}
```

---

### ⚡ Extra Notes

* Writing `[key: string]: string | undefined` can help if you expect *missing* keys.
* You can also do numeric index signatures (`[index: number]: Type`) for array-like structures.
* If you need stricter types (like specific allowed keys + dictionary), use **union + index signature** or **mapped types**.

## 🔹 Array Types in TypeScript

Arrays in TS are typed versions of JS arrays. There are **two main syntaxes**:

### 1. The Preferred Syntax

```ts
const fileExtensions: string[] = ["js", "ts"];
```

✅ Easier to read
✅ No JSX conflicts in React projects (important!)

### 2. Generic Syntax (less common in React)

```ts
const fileExtensions: Array<string> = ["js", "ts"];
```

⚠️ Can clash visually with `<div>` in JSX → avoid in React-heavy codebases.

---

## 🔹 Arrays of Objects

Just add `[]` after your custom type:

```ts
type Car = {
  make: string;
  model: string;
  year: number;
};

const cars: Car[] = [
  { make: "Toyota", model: "Corolla", year: 2002 },
  { make: "Honda", model: "Civic", year: 2005 }
];
```

Here `cars` can grow/shrink freely → arbitrary length.

---

## 🔹 Tuples (Fixed-Length Arrays)

A **tuple** is like an array, but each position has a **specific type**.

```ts
let myCar: [number, string, string];
myCar = [2002, "Toyota", "Corolla"]; // ✅ Correct
```

If you mess up:

```ts
myCar = ["Toyota", 2002, "Corolla"]; // ❌ Error: wrong order
myCar = [2002, "Toyota"];            // ❌ Missing elements
myCar = [2002, "Toyota", "Corolla", "Extra"]; // ❌ Too many elements
```

### Why tuples?

* Precise typing for *fixed-shape* data (like CSV rows, return values).
* Great for small, structured data → e.g. returning `[success, result]` from a function.

---

## 🔹 Tuple Mutability Issue

Tuples in TS are still backed by JS arrays → so `push` / `pop` technically still work, which can break the fixed length illusion:

```ts
let numPair: [number, number] = [4, 5];
numPair.push(6);   // allowed at runtime, weird in typing
```

### Fix: Use `readonly`

```ts
const numPair: readonly [number, number] = [4, 5];
numPair.push(6); // ❌ Error: Property 'push' does not exist
```

✅ Guarantees immutability
✅ Safer for data you don’t want mutated

---

## 🔹 Updating Tuples (Immutable Style)

Since `readonly` prevents modification, you create new tuples:

```ts
const numPair: readonly [number, number] = [4, 5];

// change first element → new tuple
const updated: [number, number] = [10, numPair[1]];
```

This is similar to **immutable data patterns** used in React/Redux.

---

## 🔹 Multi-dimensional Arrays

Just nest array types:

```ts
const matrix: number[][] = [
  [1, 2, 3],
  [4, 5, 6],
];
```

For 3D arrays:

```ts
const cube: number[][][] = [
  [[1, 2], [3, 4]],
  [[5, 6], [7, 8]]
];
```

---

**Summary**:

* Use `string[]` (not `Array<string>`) for arrays.
* Tuples give *fixed order & length* typing.
* Add `readonly` for immutability & safety.
* Great for function return types like `[success, data]`.

## 🔹 What Type Checking Really Means

Every time you:

* assign a value to a variable
* pass an argument into a function
* return a value from a function

TypeScript asks:

> “Does the type of `y` fit within the type of `x`?”

Think of **types as sets of possible values**:

* `number` = the set of all numbers
* `42` = the set containing just the literal value `42`
* `string[]` = the set of all arrays containing only strings

So:

* If `y`’s set is a **subset** of `x`’s set → ✅ okay
* Otherwise → ❌ type error

Example:

```ts
function alwaysFortyThree(): number {
  return 43; // ✅ 43 ∈ number
}

function wrong(): 43 {
  return 10; // ❌ 10 ∉ {43}
}
```

---

## 🔹 Static vs Dynamic Typing

* **Dynamic typing** → Types are figured out at runtime (e.g., JavaScript, Python, Ruby).
  Often called **duck typing**: if it “quacks like a duck,” it’s treated like one.

* **Static typing** → Types are declared/analyzed at build time (e.g., TypeScript, Java, C#).
  They don’t change during execution.

> **TypeScript adds static types on top of dynamic JavaScript.**

---

## 🔹 Nominal vs Structural Type Systems

This is the big one.

### 1. Nominal Typing (Java, C#)

Types are based on **name / constructor**.
If a function wants a `Car`, you must pass an instance of the `Car` class — even if another class has the exact same fields.

```java
class Car { String make; String model; int year; }
class Truck { String make; String model; int year; }

CarChecker.checkCar(new Car());   // ✅ works
CarChecker.checkCar(new Truck()); // ❌ doesn't matter that fields match
```

---

### 2. Structural Typing (TypeScript)

Types are based on **structure (shape)**.
If it “has the right properties,” it’s assignable — regardless of which class made it.

```ts
class Car { constructor(public make: string, public model: string, public year: number) {} }
class Truck { constructor(public make: string, public model: string, public year: number) {} }

function printCar(vehicle: { make: string; model: string; year: number }) {
  console.log(`${vehicle.make} ${vehicle.model} (${vehicle.year})`);
}

printCar(new Car("Toyota", "Corolla", 2002)); // ✅ works
printCar(new Truck("Ford", "F-150", 2020));   // ✅ also works
printCar({ make: "Tesla", model: "3", year: 2023, electric: true }); // ✅ extra fields fine
```

**Why?** Because TypeScript only cares:
➡️ “Does it have `make: string`, `model: string`, `year: number`?”
It doesn’t care about *where* the object came from.

---

## 🔹 Extra Properties

If you pass in more than required → still fine:

```ts
printCar({ make: "Tesla", model: "S", year: 2024, battery: "100kWh" }); // ✅
```

But if you’re creating an inline object literal, TS does **excess property checks** to help catch typos:

```ts
printCar({ make: "Tesla", model: "S", year: 2024, batteryy: "100kWh" });
// ❌ 'batteryy' not expected — probably a typo
```

---

## 🔹 Mixing Structural and Nominal-ish Behavior

* `instanceof` in TS/JS → nominal-style check (constructor-based).
* Structural typing gives flexibility; you can still restrict things to constructors if you want.

Example:

```ts
if (x instanceof Date) {
  // now TS knows x is a Date (nominal check)
}
```

So TS lets you do **both**, but defaults to **structural** because it plays nicely with plain JS objects.

##  Union andIntersection Types

* Type checking = subset check of sets of possible values.
* Static vs dynamic = when type checks happen (build time vs runtime).
* Nominal typing cares about **who made it**; structural typing cares about **what it looks like**.
* TypeScript is **structural**, which gives it flexibility with JS codebases.

## Union and Intersection Types in TypeScript

* **Types as sets** → Think of each type as a set of allowed values.

### 🔹 Union Types (`|`) = OR

* Syntax: `type AorB = A | B`
* Allowed values: any member of **either set**.
* Guarantees: we can’t assume membership in both — only that it’s one or the other.
* Example with sets:

  * Evens under 10 = `{2,4,6,8}`
  * Numbers 1–5 = `{1,2,3,4,5}`
  * Union = `{1,2,3,4,5,6,8}`
* Mental model: like **two doors with bouncers** → if you get into *either*, you’re allowed.

### 🔹 Intersection Types (`&`) = AND

* Syntax: `type AandB = A & B`
* Allowed values: only the values present in **both sets**.
* Guarantees: must satisfy all constraints at the same time.
* Example with sets:

  * Evens under 10 = `{2,4,6,8}`
  * Numbers 1–5 = `{1,2,3,4,5}`
  * Intersection = `{2,4}`
* Mental model: like **two bouncers in a row** → you must pass *both checks*.

### 🔹 Key Theme

* **Allowed values** = what can enter the set.
* **Guarantees** = what’s true for every member once inside.

👉 Union = more flexible but fewer guarantees.
👉 Intersection = stricter but more guarantees.

## Union Types, Control Flow, and Narrowing

### 🔹 Union Types in Practice

* Union types (`|`) appear frequently, especially in **control flow**.
* Example:

  ```ts
  function flipCoin(): "heads" | "tails" {
    return Math.random() > 0.5 ? "heads" : "tails";
  }
  ```

  * Only `"heads"` or `"tails"` are valid return values.
  * Nothing else (e.g. `"e"`) is allowed.

### 🔹 Tuples with Union Types

* Example: a function that might succeed or fail:

  ```ts
  type Success = ["success", { name: string; email: string }];
  type Failure = ["error", Error];
  type Result = Success | Failure;
  ```
* Accessing tuple elements directly gives only the **shared properties**.

  * E.g. both `Error` and `{ name; email }` have `name`, so TypeScript only exposes that until narrowed.

### 🔹 Narrowing with Type Guards

* Use `instanceof` or `typeof` to narrow unions:

  ```ts
  if (result[1] instanceof Error) {
    // Here, TypeScript knows it's an Error
    console.log(result[1].stack);
  } else {
    // Must be the object with name + email
    console.log(result[1].email);
  }
  ```
* Think of it like a **pie chart**: type guards slice off part of the union, leaving only what fits.

### 🔹 Discriminated Unions

* Use a **literal field** (discriminator) to connect values.
* Example:

  ```ts
  type Result =
    | { status: "success"; user: { name: string; email: string } }
    | { status: "error"; error: Error };

  function handleResult(res: Result) {
    if (res.status === "error") {
      console.error(res.error.message);
    } else {
      console.log(res.user.email);
    }
  }
  ```
* The discriminator (`status`) signals which full shape applies.
* Makes unions more precise and prevents invalid mixing.

- Union types are common because of **branching possibilities**.
- Narrowing (with guards or discriminators) unlocks their full usefulness.

## Intersection Types in Practice

* Intersection types (`&`) are the **“and”** of types.
* They only accept values that exist in **both sets**.

  * Example: `Even & LowNumber` → only `2` and `4`.
  * `6` fails (not low), `3` fails (not even).

### 🔹 Behavior vs Union Types

* **Union (`|`)** → very accepting, but weak guarantees.

  * Accepts many values, but you can’t assume much about them.
* **Intersection (`&`)** → very picky, but strong guarantees.

  * Accepts very few values, but you can assume everything true about both sets.

### 🔹 Usage

* With intersection types, you can safely pass values to **any function** expecting either of the intersected types.

  * Example: `2 | 4` works as even, works as low number, works as number.

### 🔹 Asymmetry

* **Union:** broad set of possible values, minimal guarantees.
* **Intersection:** narrow set of possible values, maximal guarantees.

### 🔹 Real-World Use

* Rarely written directly in application code.
* Most often appears **behind the scenes**:

  * `Object.assign()`
  * Object spread `{ ...obj1, ...obj2 }`
  * These merge two objects into one type = intersection of properties.

## Interfaces and Type Aliases in TypeScript

TypeScript provides **interfaces** and **type aliases** to give names to types, making code reusable and easier to manage across modules with imports and exports.

* **Type Alias Basics**

  * Allows assigning a name to a type.
  * Example: instead of repeating a noisy inline object type everywhere, define it once as `type Amount = { currency: string; value: number }`.
  * Type aliases are erased at compile time—they don’t appear in the final JavaScript.

* **Advantages**

  * Simplifies code by reducing repetition.
  * Improves readability and provides semantic meaning (like variable names for types).
  * Supports export/import for consistent type definitions across files.

* **Flexibility**

  * Type aliases can represent any type (primitives, unions, tuples, intersections, etc.).
  * Example: `type MightBeNull = string | null`.
  * This flexibility isn’t available with interfaces.

* **Practical Example**

  * Instead of writing complex tuple/union return types inline (e.g., from a function like `maybeGetUserInfo`), define them once and reuse with meaningful names.
  * Tooltips and IDE hints become clearer, showing purpose rather than raw structure.

* **Extending Type Aliases**

  * You can compose new types from existing ones using **intersection types (`&`)**.
  * Example: extend the `Date` type with an extra method:

    ```ts
    type SpecialDate = Date & { getDescription: () => string };
    ```

    This keeps all `Date` methods plus the custom `getDescription`.
  * Works like inheritance: the new type is more specific but still valid wherever a `Date` is expected.

**Key takeaway**: Use type aliases to simplify, centralize, and give meaning to complex types. They are like “variables for types” and can be composed with intersections to model more specific structures.

## Interfaces in TypeScript

Interfaces are another way to give types a name in TypeScript. They look similar to classes but contain only type information (no implementations). Interfaces are especially useful for **inheritance** and defining **contracts** for classes.

* **Basic Syntax**

  * Declared with the `interface` keyword (no `=`).
  * Only describe shapes of objects (fields and methods), not arbitrary types like unions.

* **Extends (Inheritance)**

  * Interfaces can extend other interfaces.
  * Example:

    ```ts
    interface Animal { eat(food: string): void }
    interface Mammal extends Animal { furColor: string }
    interface Hamster extends Mammal { squeak(): void }
    ```
  * Similar to class inheritance, but only for describing structure.

* **Implements (Contracts)**

  * Classes use `implements` to commit to an interface’s shape.
  * Example:

    ```ts
    interface AnimalLike { eat(food: string): void }
    class Dog implements AnimalLike {
      eat(food: string) { console.log(`Eating ${food}`) }
      bark() { console.log("Woof!") }
    }
    ```
  * If a class is missing required properties/methods, TypeScript raises an error.

* **Extends vs Implements**

  * `extends`: class → class, interface → interface (like-to-like).
  * `implements`: class → interface (a class adheres to an interface contract).
  * A class can extend **one** class but implement **multiple** interfaces.

* **Structural Typing Power**

  * Interfaces don’t require explicit inheritance.
  * Any object matching the shape is compatible.
  * Example: `PromiseLike` requires only `.then()`, so any "then-able" object works with async code.

* **When to Prefer Interfaces**

  * Use interfaces when defining contracts for classes.
  * They ensure compatibility with `implements` and inheritance rules.
  * Unlike type aliases, interfaces can’t represent unions, primitives, or arbitrary non-object types—only object-like structures.

**Key takeaway**:
Interfaces are best for describing **object shapes** and **class contracts**, supporting inheritance (`extends`) and contracts (`implements`). Use them where you want strict structural guarantees in OOP-like scenarios.