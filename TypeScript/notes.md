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

## TypeScript in Full Stack Development

- TypeScript is especially valuable when you have static types in the backend and want to maintain type safety in the frontend.
- Having types flow from backend to frontend (e.g., via GraphQL or Protobufs) reduces the need for manual alignment and helps prevent errors.
- Some companies use tools like Protobufs to generate types for both backend and frontend, ensuring consistency.
- There are full stack TypeScript courses (e.g., with GraphQL) that demonstrate this approach.

