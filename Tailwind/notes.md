# Tailwind CSS 4+
## Frontend Masters | Steve Kinney

## 1. Tailwind CSS Overview

### **What is Tailwind CSS?**

* **Utility-first CSS framework** → Uses small, single-purpose classes to style elements.
* Example: Instead of `.btn-primary`, you use classes like `bg-blue-500 text-white px-3 py-2`.
* Styles are readable directly from the class names without inspecting CSS files.

---

### **How it Works**

1. **Class stacking** → Combine multiple small classes to style a component.
2. **Build process** → Tailwind scans your code, keeps only the used classes, and generates a **minimal CSS file**.
3. **Performance advantage** → Smaller CSS bundle, easier to maintain.

---

### **Advantages**

* Fast prototyping (HTML, styles, and behavior in one place).
* Avoids CSS cascade issues.
* Easy to update site-wide styles with CSS variables.
* Works well with component systems (React, Vue, Svelte, etc.).

---

### **Criticisms**

* Long class lists can clutter HTML.
* Requires learning Tailwind’s class naming system.
* Less semantic than traditional CSS.

---

### **Component System Assumption**

* Tailwind is most effective when paired with **reusable components**.
* Changes in a component update all instances (avoids repetitive class application).

---

### **Framework & Tooling Agnostic**

* Works with any framework (or none) since it’s just CSS.
* Uses **CSS variables** to map design tokens from tools like Figma.

---

### **Build Process (Oxide)**

* Tailwind’s internal Rust tool scans files → keeps only used classes → removes unused ones.
* Output: Optimized, concise CSS file.

---

### **Installation**

* Requires build tooling (Vite, Webpack, PostCSS) for optimal use.
* **Basic steps**:

  1. Install Tailwind via npm.
  2. Configure `tailwind.config.js`.
  3. Import Tailwind in root CSS file:

     ```css
     @tailwind base;
     @tailwind components;
     @tailwind utilities;
     ```
* **CDN Option** → For quick testing (Tailwind Play, script tag).

---

### **Key Takeaways**

* Tailwind is a **CSS-first, framework-agnostic** system.
* Best used with **components + build tooling**.
* Trades semantic class names for **speed, consistency, and bundle size efficiency**.

## 2. How Tailwind CSS works

Tailwind scans your project for **full class names** in plain text and includes only those in the final CSS. It does **not** analyze your code’s logic — it’s essentially pattern-matching strings.

* ✅ **Works:** Writing the full class name anywhere in your HTML, JS, or TS files (e.g., `const success = "bg-green-400";`).
* ❌ **Doesn’t work:** Dynamically building class names with concatenation or template strings (e.g., `` `bg-${color}-400` ``) — Tailwind won’t detect them.
* **Safelisting:** If you know some classes won’t appear directly in your code (like ones injected from a third-party library), you can explicitly safelist them so Tailwind doesn’t strip them out.
* **Plugins & customization:** You can extend Tailwind via JavaScript-based plugins and customize colors, spacing, fonts, etc. Everything is configurable.
* **Ignore list:** Tailwind ignores certain files by default (e.g., `.gitignore` entries, CSS files, lock files).

If styles aren’t showing up, **the first debugging step** should be: *“Did Tailwind strip this class because it didn’t see it in my code?”*

## 3. Tailwind CSS Best Practices & Layers

* **CSS Layers in Tailwind:**

  * **Theme layer:** Defines CSS variables (colors, spacing, fonts) → becomes Tailwind utility classes.
  * **Base layer:** Styles raw HTML elements (body, lists, inputs, etc.).
  * **Components layer:** Styles specific UI components (e.g., buttons).
  * **Utilities layer:** Adds one-off utility classes to extend Tailwind.

* **Customization:**

  * Override or add colors, fonts, and sizes in the **theme layer** to generate new Tailwind classes.
  * Brand-specific tokens (e.g., `brand`, `success`, `error`) can replace defaults like `blue`.

* **Best practice:**

  * Keep base HTML elements minimal and style through utility classes in markup for flexibility.
  * Use base layer changes when migrating from older codebases or enforcing consistent defaults.

* **IntelliSense & tooling:**

  * Use the **Tailwind IntelliSense plugin** in VS Code for class autocompletion, especially with custom utilities or theme variables.

* **CSS Layer Order in Tailwind:**

  1. Theme
  2. Base
  3. Components
  4. Utilities

  * Order is predefined by Tailwind; the order you write them in your CSS doesn’t matter.

## 4. Theme Layer & Custom Colors

* **Purpose:** Lets you define your own design tokens (colors, fonts, spacing).
* **Example:** You can add a `brand` color alongside Tailwind’s default palette.
* **Shade Pattern:** Tailwind uses numbered shades (`blue-600`, `blue-500`, etc.), but you can use your own naming like `brand`, `brand-light`, `brand-dark`.
* **Benefits:**

  * Once set in the **theme layer**, you can use it anywhere:

    ```html
    <div class="bg-brand text-white"></div>
    ```
  * Changing the CSS variable updates it **globally**.

---

### **Variants (Responsive, State, etc.)**

* Tailwind has **built-in responsive breakpoints**:

  * `sm`, `md`, `lg`, `xl`, `2xl`.
  * Prefixing with `md:` applies styles only from that breakpoint upward.

  Example:

  ```html
  <div class="w-full md:w-1/2"></div>
  ```

  → Full width on mobile, half width from `md` up.

* **State variants** like `hover:`, `focus:`, `active:` can be **stacked** with responsive variants.

  Example:

  ```html
  <button class="bg-brand md:hover:bg-brand-dark">
    Click Me
  </button>
  ```

  → Changes background color only when hovered on **medium and larger screens**.

* **Why it’s powerful:**
  Instead of verbose CSS:

  ```css
  @media (min-width: 768px) {
    .btn:hover {
      background-color: var(--brand-dark);
    }
  }
  ```

  You write:

  ```html
  <button class="md:hover:bg-brand-dark">Click Me</button>
  ```

## 5. Tailwind Patterns & Anti-Patterns

### **Anti-Patterns**

* **One-off classes without `@utility`**

  * Works for direct usage (`my-button`) but **breaks with variants** (`hover:my-button` won’t work).
* **Excessive arbitrary values (`[value]` syntax)**

  * Great for rare, one-time needs.
  * Overuse leads to hard-to-maintain code and painful refactoring.

### **Patterns**

* **Use `@utility` for custom classes**

  * Makes them compatible with variants (`hover:`, `md:`, etc.).
* **Define theme variables for reusable styles**

  * Ensures consistency and easy global changes.
* **Keep styling in markup**

  * Most Tailwind usage should happen in HTML/JSX/Svelte/Angular templates.
  * Limit direct CSS edits except for theme tweaks.
* **Custom utilities & variants**

  * Possible to define your own responsive or state variants for special cases.

## 6. Tailwind Setup & Tools Overview

### **Project Setup**

* Clone the **Tailwind Skatepark** repo.
* Install dependencies:

  ```bash
  npm install
  npm start
  ```
* Project uses **Svelte** for simplicity (React/Angular concepts still apply).

### **Recommended Tools**

* **Tailwind CSS IntelliSense** (VS Code)

  * Autocompletes Tailwind classes.
  * Sorts classes automatically to prevent style order debates.
* **Prettier Plugin** (optional)

  * Ensures consistent class name ordering.
* **Color Palette Tools**

  * UI Colorless (generate Tailwind palettes, export as CSS variables).
  * Semantic color palette generator (e.g., `error`, `warning`, `destructive` instead of `red`, `blue`).
  * Figma plugin for syncing design & CSS variables.

### **Preflight**

* Tailwind’s **Preflight** strips browser default styles.
* Normalizes styles across browsers.
* Leaves elements like buttons looking unstyled, ready for Tailwind utilities.

### **Future Topics**

* JavaScript libraries for merging/diffing class names in design systems.
* Handling style overrides (e.g., default blue button overridden with pink).

## Note Guide: Tailwind Card Demo

### **Objective**

* Build and style a reusable **card component** using Tailwind utilities.
* Practice rapid prototyping with borders, backgrounds, typography, and spacing.

---

### **Core Steps**

1. **Start with the card container**

   * Add a **border**: `border` or `border-2`
   * Add **padding**: `p-4` (even padding all around)
   * Add **rounded corners** (optional): `rounded`, `rounded-lg`, etc.
   * Add a **background**: `bg-slate-50`, `bg-gray-100`, or similar.

2. **Typography**

   * **Heading (h2)**

     * Size: `text-lg`, `text-xl`, etc.
     * Weight: `font-semibold` or `font-bold`.
   * **Paragraph**

     * Add **margin top** for spacing: `mt-2`.
     * Adjust font size: `text-base`, `text-sm`.
     * Optional line/letter spacing utilities.

3. **Colors**

   * Border: `border-slate-200`, `border-gray-300`, or custom theme color.
   * Background: subtle tone (`bg-slate-50`) to distinguish card.

---

### **Key Tailwind Utilities**

* **Borders**: `border`, `border-2`, `border-color`
* **Spacing**: `p-*`, `px-*`, `py-*`, `m-*`, `mt-*`, etc.
* **Rounded Corners**: `rounded`, `rounded-md`, `rounded-lg`
* **Backgrounds**: `bg-slate-*`, `bg-gray-*`, custom theme colors
* **Typography**:

  * Size: `text-xs` → `text-9xl`
  * Weight: `font-light`, `font-medium`, `font-semibold`, `font-bold`
  * Line Height & Spacing: `leading-*`, `tracking-*`

---

### **Tips & Mindset**

* No need for back-and-forth CSS files → style directly in markup.
* Explore class autocompletion (`text-`, `font-`, `bg-`) to discover options.
* Subtle changes (border width, padding, background shade) make the card feel polished.
* **Rounded vs. square corners** is a design preference—use what feels right.
* Think of **button = hello world**, **card = next level component** when experimenting.


## Note Guide: Tailwind Card Layout & Spacing

### **Objective**

* Learn to layout **multiple components** (cards) using Tailwind utilities.
* Explore spacing, dividers, and layout techniques (space, divide, flexbox, grid).

---

### **Problem**

* Multiple cards **stack tightly** → looks cramped.
* Need ways to **add breathing room** between elements.

---

### **Tailwind Spacing Utilities**

1. **Space Between Elements**

   * `space-y-*` → vertical spacing (stacks)
   * `space-x-*` → horizontal spacing (rows)
   * Example:

     ```html
     <div class="space-y-4">
       <div class="card">Card 1</div>
       <div class="card">Card 2</div>
     </div>
     ```
   * Works by applying margin to **all but last child**.

2. **Dividers**

   * `divide-y` → horizontal dividers between stacked items
   * `divide-x` → vertical dividers between inline items
   * Example:

     ```html
     <div class="divide-y divide-gray-200">
       <div>Item 1</div>
       <div>Item 2</div>
     </div>
     ```
   * Adds **visual separators**; color can be customized.

---

### **Flexbox vs. Space/Divide**

* **Space utilities**:

  * Quick, margin-based solution.
  * Great when you just need consistent gaps.

* **Flexbox (`flex`, `justify-*`, `items-*`)**:

  * More control over alignment & distribution.
  * Every child becomes a flex item (can change behavior).

* **Grid (`grid`, `grid-cols-*`, `gap-*`)**:

  * Most flexible for complex layouts.
  * Use when arranging multiple rows/columns of cards.

---

### **Tips**

* **Default to `space-y` or `space-x`** for simple spacing.
* Use **`divide` sparingly** (rarely used in practice).
* Reach for **flexbox/grid** when you need more than just spacing.
* Before writing custom CSS, check if Tailwind has a utility—**it probably does**.

---

### **Progression for Learning**

1. Start with **space utilities** (`space-y`, `space-x`).
2. Try **divide utilities** for visual separators.
3. Explore **flexbox** for alignment.
4. Experiment with **grid** for multi-card layouts.

### Form Input

* Inputs in Tailwind are just elements styled with utility classes; unlike Bootstrap, they don’t come with a strong preset “look.”
* You build input components (label + input + optional description/error) with utility classes, and reuse via templating or Storybook instead of repeating styles.
* Use `block` to stack label/input vertically.
* Font weights: `font-medium` (500), `font-semibold` (600), `font-bold` (700), etc.
* Color palettes (`slate`, `gray`, etc.) are customizable.
* Styling inputs: `rounded`, `p-*` for padding, `outline-*` for focus states, `bg-white`, `w-full`.
* Use `space-y-*` on parent containers to space children instead of repetitive margins.
* Use `focus:*` variants for focus states.
* Placeholder styling supported via `placeholder:*` and `placeholder-italic`.
* Negative values (`-mt-2`, `-mb-4`, etc.) are supported for most spacing utilities.
* For outlines vs rings: use `outline-*` for outside highlight, `ring-*` for more flexible focus styles.
* Use `space-*` for simple spacing, flexbox when alignment/justification is needed.

---

### Demo Snippet

```html
<div class="space-y-2 w-full max-w-sm">
  <label for="email" class="block text-slate-700 font-medium">
    Email Address
  </label>
  <input
    id="email"
    type="email"
    placeholder="you@example.com"
    class="block w-full rounded-md bg-white px-3 py-2
           outline outline-1 outline-slate-300
           focus:outline-2 focus:outline-blue-400
           placeholder:text-slate-400 placeholder:italic"
  />
  <p class="text-sm text-slate-500">We’ll never share your email.</p>
  <p class="text-sm text-red-600">This field is required.</p>
</div>
```

## Input States and Variants in Tailwind

* Inputs have many states (required, valid, invalid, focus, focus-visible, etc.), mapped to CSS pseudo-classes.
* `invalid` marks required empty fields as invalid immediately (not user-friendly).
* `user-invalid` and `user-valid` trigger **after user interaction** (focus + blur), solving premature error display.
* Most styling is done for “sad states” (invalid, out-of-range) but positive states (valid, success) can be styled too.
* Tailwind utilities (`invalid:*`, `user-invalid:*`, `focus:*`, etc.) replace verbose CSS selectors, keeping logic in class lists instead of custom CSS/JS.
* Using these avoids manual state management in frameworks (React, Angular, etc.), reducing complexity.
* Some pseudo-classes like `:has` (supported in modern browsers) enable even more advanced styling without JS.

---

### Demo Snippet

```html
<div class="space-y-3 w-full max-w-sm">
  <!-- Required input with validation states -->
  <label for="email" class="block text-slate-700 font-medium">Email</label>
  <input
    id="email"
    type="email"
    required
    placeholder="you@example.com"
    class="block w-full rounded-md px-3 py-2
           outline outline-1 outline-slate-300
           focus:outline-2 focus:outline-blue-400
           placeholder:text-slate-400
           invalid:outline-red-500
           user-invalid:outline-red-600
           user-valid:outline-green-500"
  />
  <p class="text-sm text-slate-500">We’ll never share your email.</p>
</div>
```

✅ Behavior:

* Default: neutral outline.
* While focused: blue outline.
* If left empty → `user-invalid` adds red outline only **after blur**.
* If valid email entered → `user-valid` adds green outline.

## Focus Within & Checkbox Styling in Tailwind

* **`focus`** → Styles the element when it’s directly focused.
* **`focus-visible`** → Styles only when focus comes via **keyboard navigation**, not mouse clicks.
* **`focus-within`** → Styles a **parent container** if *any* child element inside is focused.
* Great for wrapping inputs, checkboxes, or grouped UI where the whole container should highlight.
* **Checkbox styling**:

  * Use `accent-*` to change the checkmark color (`accent-purple-400`, etc.).
  * Works for checkboxes, radios, and range inputs.
* **Practical use cases**:

  * Highlighting form groups when any field inside is active.
  * Making custom UI components (e.g., input with a button inside) behave as a single focusable unit.
  * Styling parent containers consistently without extra JS.

---

### Demo Snippet

```html
<div class="p-4 rounded-lg border border-slate-300 focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-blue-200">
  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" class="accent-purple-500 w-5 h-5" />
    <span class="text-slate-700">Subscribe to newsletter</span>
  </label>
</div>

<div class="mt-4 p-4 rounded-lg border border-slate-300 focus-within:border-green-500 focus-within:ring-2 focus-within:ring-green-200">
  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" class="accent-green-500 w-5 h-5" />
    <span class="text-slate-700">Enable notifications</span>
  </label>
</div>
```

✅ Behavior:

* Clicking or tabbing into the checkbox applies `focus-within` to the **parent container**, highlighting the box.
* `accent-purple-500` / `accent-green-500` changes the checkmark color.
* Works seamlessly across multiple checkboxes — only the parent of the focused one highlights.

## Group & Peer in Tailwind

* **`group`**

  * Placed on a **parent** element.
  * Enables children to react to parent states (`group-hover`, `group-focus`, etc.).
  * Example: hover anywhere on a card → change title color & enlarge button.
* **`peer`**

  * Placed on an **input (or any element)**.
  * Allows **subsequent siblings** to react to its state (`peer-invalid`, `peer-checked`, etc.).
  * Limitation: only works on elements that **come after** the peer in DOM order.
* **Use cases**:

  * `group`: Coordinated hover/focus effects across entire components (cards, menus, buttons inside containers).
  * `peer`: Form validation or input-driven styling (checkbox → strike through label, input invalid → show error).
* **Gotchas**:

  * `peer` won’t affect elements before it in DOM order. Workarounds include reordering, flex-reverse, or modern CSS (`:has()` in newer browsers).

---

### Demo Snippet

```html
<!-- Group Example -->
<div class="group border rounded-lg p-4 hover:shadow-lg transition">
  <h2 class="text-lg font-semibold group-hover:text-blue-600">
    Premium Plan
  </h2>
  <p class="text-slate-600">Get access to all features.</p>
  <button class="mt-3 px-4 py-2 bg-blue-500 text-white rounded-md transform transition group-hover:scale-105">
    Buy Now
  </button>
</div>

<!-- Peer Example -->
<div class="mt-6">
  <input type="checkbox" id="todo" class="peer hidden" />
  <label for="todo" class="cursor-pointer text-slate-800 peer-checked:text-green-600 peer-checked:line-through">
    Finish Tailwind lesson
  </label>
</div>
```

✅ Behavior:

* Hover anywhere on the **card** → the title changes color & button grows.
* Check the **checkbox** → label turns green with a strikethrough.

## Tailwind CSS: `has()` Utility

* **`group`** → Children style themselves based on the **parent state** (hover, focus, active, etc.).
* **`peer`** → Siblings style themselves based on the **state of a sibling before them**.
* **`has()`** → A parent can style itself based on the **state of its children**.
* Supported in modern browsers (not IE11, poor in Opera Mini).
* Replaces many JavaScript use cases (form validation, conditional styling, dynamic layout).
* **Powerful when combined** with `group` (children ↔ parent awareness).

### Key Points

* **Example use cases**:

  * Change parent styling when a child input is `:checked` or `:invalid`.
  * Update card layout dynamically (e.g., if it **has** an `<img>`).
  * Toggle styling based on whether a `<details>` element is open.
  * Disable/enable submit buttons based on form validity (pure CSS).
* **Mixing utilities**:

  * `group` → parent → children.
  * `has()` → children → parent.
  * Together → **bidirectional state awareness**.

---

### Demo Snippet

```html
<div class="p-6 border rounded-lg has-[input:checked]:bg-green-100">
  <label class="flex items-center space-x-2">
    <input type="checkbox" class="peer">
    <span class="peer-checked:line-through">Accept terms</span>
  </label>
  <p class="text-sm text-gray-500 group-has-[input:checked]:text-green-700">
    Checkbox checked → parent background + text change
  </p>
</div>
```

✅ Features in the snippet:

* **`has-[input:checked]`** → Parent turns green if any child input is checked.
* **`peer-checked`** → Sibling text line-through when checkbox is checked.
* **`group-has-[...]`** → Demonstrates chaining `group` + `has` for more advanced styling.

## Using `:has` and `group` in Tailwind to Show Required Field Indicators

The **`:has` selector** lets a parent element style itself based on its children. Combined with Tailwind’s `group`, you can style labels depending on whether their associated input fields are required—without writing any JavaScript.

### Key Idea

* `group`: Allows children to style themselves based on their parent’s state.
* `:has`: Allows the parent to style itself depending on its children.
* Together, they make it possible to handle patterns (like required fields) that previously needed JavaScript or hacky workarounds.

### Demo Snippet (HTML body only)

```html
<div class="group flex items-center gap-2">
  <label class="after:content-['*'] after:ml-1 after:text-red-600 group-has-[input:required]:after:inline-block group-has-[input:required]:after:text-red-600">
    Email
  </label>
  <input type="email" required class="border p-2 rounded" />
</div>

<div class="group flex items-center gap-2 mt-4">
  <label class="after:content-['*'] after:ml-1 after:text-red-600 group-has-[input:required]:after:inline-block group-has-[input:required]:after:text-red-600">
    Username
  </label>
  <input type="text" class="border p-2 rounded" />
</div>
```

### How It Works

* By default, the label won’t show a red dot or asterisk.
* When the `input` inside has `required`, the label’s `after` pseudo-element becomes visible.
* All styling is done purely in **Tailwind + CSS**, no JavaScript needed.

## File Tree with `peer` in Tailwind

The conversation is about simulating a **file/folder picker** where checking the **parent folder checkbox** gives the *visual appearance* that its children (files) are also selected — **without writing JavaScript**.

This is possible in **Tailwind CSS** using `peer` and structural hierarchy. However, it's important to note:

* This only affects **visuals**, not actual checked states of child inputs.
* For true accessibility (ARIA, screen readers), you’d still need **JavaScript**.

---

### Demo Snippet (HTML Body Only)

```html
<div class="p-4 space-y-4">
  <!-- Folder -->
  <div class="space-y-2">
    <label class="flex items-center space-x-2">
      <input type="checkbox" id="folder-1" class="peer" />
      <span class="font-semibold">📁 Project Folder</span>
    </label>

    <!-- Files inside the folder -->
    <ul class="ml-6 space-y-1">
      <li class="flex items-center space-x-2 peer-checked:opacity-50 peer-checked:pointer-events-none">
        <input type="checkbox" disabled />
        <span>📄 index.html</span>
      </li>
      <li class="flex items-center space-x-2 peer-checked:opacity-50 peer-checked:pointer-events-none">
        <input type="checkbox" disabled />
        <span>📄 style.css</span>
      </li>
      <li class="flex items-center space-x-2 peer-checked:opacity-50 peer-checked:pointer-events-none">
        <input type="checkbox" disabled />
        <span>📄 script.js</span>
      </li>
    </ul>
  </div>

  <!-- Another sibling file -->
  <div class="flex items-center space-x-2">
    <input type="checkbox" />
    <span>📄 readme.md</span>
  </div>
</div>
```

---

✅ Checking **Project Folder** dims and disables its children files (visually representing "all selected").
⚠️ Child checkboxes aren’t *actually* checked — they’re just styled to look inactive/selected.

## Input Field with Attached Button (Accessible UI)

* Use a **screen-reader-only label (`sr-only`)** for accessibility while keeping the interface clean.
* Wrap the input and button inside a **flex container** to style them as a single unit.
* Apply **Tailwind utilities** for padding, colors, and rounded corners.
* Add **focus states with `ring`** for better UX.
* Use the **`:has()` selector** to style parent based on child input validity (e.g., highlight invalid states).

---

### Demo Snippet (HTML Body Section Only)

```html
<div class="p-6 max-w-md">
  <form class="flex items-center gap-2 outline outline-slate-600 rounded-2xl px-3 py-1.5 has-[input:invalid]:ring-2 has-[input:invalid]:ring-red-600 focus-within:ring-2 focus-within:ring-purple-500">
    <label for="task" class="sr-only">New Task</label>
    <input 
      id="task" 
      type="text" 
      required 
      placeholder="Add a new task..."
      class="flex-grow bg-transparent outline-none px-2 py-1"
    >
    <button 
      type="submit"
      class="bg-purple-600 text-white px-4 py-1.5 rounded-xl hover:bg-purple-700 transition"
    >
      Add
    </button>
  </form>
</div>
```
