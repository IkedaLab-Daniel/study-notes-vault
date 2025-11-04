# React and TypeScript v2

## React and TypeScript Course Introduction

* **Instructor:** Steve, frontend engineering lead at **Temporal**, Denver, Colorado, originally from **New York/New Jersey**.
* **Team Focus:** Developer Tools — UI, VS Code plugins, and frontend engineering.
* **Course Focus:** Learning **TypeScript in React**, not just TypeScript alone.
* **Assumed Knowledge:** Familiar with React basics; no need to be a TypeScript expert.

### Key Themes

* **Philosophy & Practice:** Understand *why* and *how* TypeScript works with React.
* **Editor-Driven Learning:** Use **VS Code IntelliSense** to explore, hover, and learn directly in the editor.
* **Positive Feedback Loop:** Learn TypeScript by *building React components*.

### Learning Journey

* Begin with simple examples → progress to advanced TypeScript & React patterns.
* Explore conversion from **PropTypes** to **TypeScript types**.
* Use TypeScript to catch errors early instead of relying on console debugging.
* Appreciate **autocomplete** and **type safety** for preventing typos (e.g., Redux action types).

### Real-World Benefits

* Faster debugging and fewer runtime errors.
* Improved collaboration on large codebases with **instant compile-time feedback**.
* Encourages **simpler, clearer code** — less “magic,” more maintainability.

### Additional Notes

* **Setup:** Course repo and sandboxes provided for hands-on learning.
* **React 18 Updates:** Adjustments from React 17 (e.g., `React.FunctionComponent` no longer assumes `children`).
* **TypeScript Evolution:** Each version simplifies setup and boosts developer experience.
* **Final Advice:** Leverage your editor — modern TypeScript and React development thrives on *in-editor guidance*.


## React Component with TypeScript

### 🧠 1. What Makes a TypeScript Component?

* The only main difference between a JavaScript React component and a TypeScript React component is **the file extension: `.tsx` instead of `.jsx`**.
* `.tsx` files allow you to use TypeScript features (types, interfaces, generics) in your React components.

---

### 🧩 2. TypeScript Tries to Infer Everything

* TypeScript automatically **infers** as much as possible — you don’t need to manually type everything.
* Example:

  ```tsx
  function NameBadge() {
    return <div>Hello!</div>;
  }
  ```

  TypeScript *knows* this function returns a JSX element, even if you don’t explicitly tell it.

---

### ⚙️ 3. Adding Props with Types

When you add props, TypeScript can’t infer what those are — you need to define them.

Example:

```tsx
function NameBadge({ name }: { name: string }) {
  return <h1>Hello, {name}!</h1>;
}
```

If you try to use `<NameBadge />` without passing a `name`, TypeScript will immediately throw an error.

✅ This prevents runtime errors like `"Cannot read property '...' of undefined"`.

---

### 🚨 4. Strict Mode = “Be Honest With Me”

* `strict: true` in your `tsconfig.json` forces TypeScript to check everything carefully.
* It’s more work at the start but helps catch bugs **early** — especially missing props, wrong types, or possible `undefined` returns.

---

### 🧾 5. Defining Function Types

You can define the type of a function’s parameters or its return value:

```ts
function double(num: number): number {
  return num * 2;
}
```

TypeScript would usually infer that the return type is `number`, but explicitly declaring it can help you catch mistakes.

---

### 🧱 6. TypeScript vs. PropTypes

* Old React used `PropTypes` to check prop types **at runtime**.
* TypeScript checks them **at compile time**, before running the app — faster and safer.
* You don’t need the `prop-types` package when using TypeScript.

---

### 🧩 7. Working with JavaScript Files

* You can mix JS and TS files during migration by turning on:

  ```json
  "allowJs": true
  ```

  in `tsconfig.json`.
* TS can import JS files fine, but if a TS file imports JS, the imported stuff will have the `any` type (no type safety).

---

### ⚡ 8. Helpful Editor Integration

* Editors like VS Code instantly show **red squiggles** when types don’t match.
* You don’t have to refresh or check the console — you see problems as you type.
* It’s also great for refactoring safely.

---

### 🧩 9. Typical `tsconfig.json` Settings

Common useful settings:

```json
{
  "compilerOptions": {
    "target": "ES5",
    "jsx": "react-jsx",
    "strict": true,
    "allowJs": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true
  }
}
```

* `allowJs` → for migrating mixed JS/TS apps
* `strict` → catches all possible unsafe behavior
* `noFallthroughCasesInSwitch` → ensures all cases are handled

---

### 🧠 10. Key Mindset Shift

> “TypeScript is not supposed to get in your way — it’s there to **help you**.”

* You don’t need to over-type everything.
* Let TypeScript infer what it can.
* Add types only where TypeScript cannot deduce intent (e.g., props, complex logic, API data).