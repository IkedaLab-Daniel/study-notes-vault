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
