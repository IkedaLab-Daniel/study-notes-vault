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
