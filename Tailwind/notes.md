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
