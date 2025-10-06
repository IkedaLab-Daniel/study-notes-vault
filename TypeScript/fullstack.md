# Fullstack TypeScript, v2 (feat. Zod)

## Full Stack TypeScript — Lesson 1 Summary

* **Instructor:** Steve Kinney
* **Topic:** TypeScript across multiple codebases, focusing on maintaining type safety between systems (frontend, backend, database).

### Key Concepts

* **Reality of Multiple Codebases:**

  * Each codebase (frontend, backend, database) can be perfectly typed individually.
  * Problems arise **in the middle** — when data crosses boundaries (e.g., API calls).
  * Much of TypeScript’s type safety relies on **trust** that data from other systems matches expected types.

* **Goal:**

  * Move from *optimistic trust* (“I hope this matches my type”) to *pessimistic trust* (“I know this matches my type because I validated it”).
  * Introduce strategies to verify and validate data at runtime across systems.

* **Common Pain Points:**

  * Client assumes API responses match the expected shape.
  * Server assumes incoming requests have the correct structure.
  * Databases might store or return data in unexpected formats (e.g., booleans as `1/0`).

### The Type Gap Problem

* **Fetch Example:**

  * `response.json()` returns `any`.
  * Even if you cast it (`as Task`), it’s just “pretend” type safety—TypeScript trusts your declaration but doesn’t validate data.
  * The danger: runtime errors despite “safe” TypeScript code.

* **Server Example:**

  * Express `req.body` is also `any`.
  * Backend trusts that client payloads match expectations.

* **Result:**

  * Both client and server rely on *assumptions* about data structure.
  * Leads to runtime errors when assumptions don’t match reality.

### Common Causes of Failures (Anecdotal “Pie Chart”)

* **53%** — Backend changed API without informing frontend.
* **29%** — Dependencies upgraded, altering API behavior.
* **Rest** — Random issues (like deleting an S3 bucket).

### Objective of the Lesson

* Learn to **bridge the type gap** between systems.
* Ensure that API changes or data mismatches don’t silently break your app.
* Explore techniques and tooling to validate data at runtime.
* Build confidence in full-stack type safety so your “pager doesn’t go off at 2 AM.”

### Additional Resources

* Steve provides a **course notes website** and **GitHub repo** with all examples.
* Includes extended notes beyond what’s covered in the session.

## Type Guards and Runtime Validation with Zod

* **Type Guards:**
  Type guards help verify that data matches expected types at runtime. Unlike compile-time checks, they confirm actual data integrity. However, writing manual type guards becomes messy, especially for nested or complex objects.

* **Problem with `any` and `unknown`:**
  `any` bypasses all type checks, spreading unsafe assumptions. Using `unknown` is safer but forces manual checks for every property, leading to verbose and error-prone code.

* **Example – Task Object Validation:**
  Even for a simple “task” object, you must ensure it’s not `null`, is an object, and has properties like `id`, `title`, and `completed` of the correct types. This manual validation quickly becomes unmanageable for large or nested objects.

* **Solution – Zod Library:**
  Zod simplifies runtime validation by defining schemas that describe what data should look like.
  Example schema:

  ```ts
  const TaskSchema = z.object({
    id: z.number(),
    title: z.string(),
    completed: z.boolean(),
  });
  ```

  * Can coerce types (e.g., `"1"` → `1`).
  * Supports unions, optionals, partials, custom error messages.
  * You can infer TypeScript types directly from Zod schemas using `z.infer<typeof TaskSchema>`.

* **Parsing and Validation:**

  * `parse()` throws an error if data doesn’t match the schema.
  * `safeParse()` returns an object like `{ success: boolean, data?, error? }` without throwing.
  * Once data passes validation, it is guaranteed to match the inferred type.

* **Benefits of Zod:**

  * Fewer lines of code and higher reliability than manual guards.
  * Ensures type safety across API boundaries and user input.
  * Reduces runtime bugs caused by invalid or unexpected data.

* **Alternatives:**

  * **Yup:** Similar schema definition and validation but uses `.validate()` instead of `.parse()`.
  * **io-ts:** Uses `.decode()` for similar purposes.
  * All share the same goal — validate runtime data to ensure consistency between types and reality.

* **Key Insight:**
  Using schema validation tools like Zod bridges the gap between compile-time type safety and real-world runtime data, ensuring your app behaves predictably even when APIs or users don’t.

## Exploring Zod and Its Ecosystem

* **Zod Ecosystem:**
  Zod integrates with many tools and frameworks, such as **React Hook Form**, **Formik**, and **SvelteKit**.

  * You can reuse the same schema for **frontend form validation** and **backend API validation**, ensuring consistent rules across your app.
  * Schemas can also be converted into **JSON Schema** or **TypeScript types**, providing flexibility across tools.

* **Community and Reusability:**
  Before coding manual validators, check if Zod or its plugins already provide them—many tedious validation tasks are already solved by the community.

* **Beyond TypeScript:**
  Zod can perform checks that TypeScript alone cannot:

  * Validate **email formats**, **positive numbers**, and **string patterns**.
  * Use **coercion** to convert compatible types (e.g., `"42"` → `42`).
  * Enforce **minimum/maximum lengths**, **specific string literals**, or **enumerated values** (like `"red" | "green" | "blue"`).

* **Advanced Features:**

  * **Tuples:** Validate fixed-length arrays with specific types (e.g., `[string, number]`), useful for structures like React’s `useState` pair.
  * **Unions and Intersections:** Combine multiple types (`string | number`) or merge schemas.
  * **Composition:** Reuse and nest schemas for structured objects, extend them like interfaces, or pick specific fields.

* **Power of Composition:**
  Zod lets you build modular, reusable schemas for complex, nested objects—avoiding repetitive definitions and keeping validation logic consistent and clean.

* **Summary Insight:**
  Zod extends TypeScript’s static type system into runtime, enabling full data validation, transformation, and composition. It provides a single source of truth for data integrity across backend, frontend, and APIs.

## Hands-On with Zod: Building and Testing Schemas

* **Project Structure Overview:**
  The app has a `client` (React), a `server` (Express), a `shared` folder for reusable logic, and an `exercises` folder for Zod practice.

  * You’ll focus on the `exercises/zod` folder to practice writing and testing schemas.
  * Tests are set up with `.todo` markers—remove them to start running failing tests and apply **test-driven development (TDD)**.

* **Getting Started:**

  * Run `npm test` to execute tests.
  * Remove `.todo` from test cases one by one to reveal failing tests.
  * The goal: write schemas that make the tests pass (turn red → green).

* **First Schema Example:**
  Create a basic object schema for a **user**:

  ```js
  const userSchema = z.object({
    name: z.string(),
    age: z.number().int().positive()
  });
  ```

  * Ensures `name` is a string and `age` is a **positive integer**.
  * Zod gives more granular checks than TypeScript (e.g., integer-only or positive numbers).
  * You can infer a TypeScript type using `z.infer<typeof userSchema>`.

* **Optional Fields and Defaults:**
  Add optional properties with default values:

  ```js
  age: z.number().min(0).optional().default(0)
  ```

  * Order of chaining matters in Zod (`.optional().default(0)` must be applied correctly).
  * When a default is set, the property is no longer optional in the inferred TypeScript type.

* **Referencing Other Schemas:**
  Schemas can **reference and compose** others:

  ```js
  const addressSchema = z.object({
    street: z.string(),
    city: z.string(),
    zip: z.string().length(5).regex(/^\d+$/),
    apartment: z.string().optional()
  });

  const userProfileSchema = z.object({
    name: z.string(),
    addresses: z.array(addressSchema)
  });
  ```

  * Enables reusability and composition for complex data models.

* **Unions and Literals:**
  Use **unions** to represent multiple valid shapes:

  ```js
  const anonymousSchema = z.literal("anonymous");
  const userSchema = z.object({
    id: z.number(),
    name: z.string()
  });

  const userIdentitySchema = z.union([anonymousSchema, userSchema]);
  ```

  * Accepts either the literal `"anonymous"` or an object with `id` and `name`.

* **Key Takeaways:**

  * Zod complements TypeScript by validating data **at runtime**.
  * Order of chaining matters for modifiers like `.optional()` and `.default()`.
  * Schemas can reference, compose, and reuse one another for scalability.
  * Zod enables **TDD-style validation**—you can build schemas progressively by running tests and fixing validation logic.
