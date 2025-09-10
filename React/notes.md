# Intermediate React, v6
[Course Link](https://frontendmasters.com/courses/intermediate-react-v6/)

## Course Context

* Continuation of Complete Intro to React v9, but v5 or older not required.
* Focused on newer React concepts: React Server Components, performance, transitions.
* v5 still valid for Redux/TypeScript.
* Designed as a companion to Intro to React v9.

## Course Structure

### Part 1: React Server & Rendering

* Review client-side React, static site generation, server-side rendering.
* React Server Components (RSCs): without framework and with Next.js.

### Part 2: Performance

* Make apps performant (actual) and feel performant (perceived).

## Audience

* Not for first-time coders or first JavaScript learners.
* Good for those with React fundamentals or Intro to React v9.
* Some Node.js exposure helpful since RSCs need it.

## Teaching Style & Resources

* First half: build from scratch.
* Second half: starter repos provided.
* Completed repos available for comparison.
* Starter repos are minimal boilerplate, completed repos are full examples.

## About Brian Holt

* 10+ years React experience.
* Works at NEON (serverless Postgres).
* Past experience: Snowflake, Microsoft, LinkedIn, Netflix, Reddit.
* Background in frontend and Node.js.
* Hobbies: snowboarding, cycling, beers, scotch, Marvel Rivals.

## Setup & Tools

* **Node.js**: Requires Node ≥20.16 (using v22.14 LTS).
* **Node version managers**: Fast Node Manager (preferred), NVM, or Volta.
* **Alternative runtimes**:

  * Bun: \~65% chance course works (not tested).
  * Deno: \~50% chance it won’t work.
* **Editor**: VS Code (primary), occasionally Copilot and Cursor.
* **AI completions**: Disabled during course for focus.
* **Browser**: Firefox (to support non-Chromium).
* **Terminal**: VS Code terminal or terminal.app.
* **Fonts & Themes**:

  * Editor: MonaLisa (paid) or Cascadia Code (free).
  * Terminal: zsh, Dracula theme, Starship prompt, Nerd Fonts.

## AI Disclaimer

* All course text/code written by Brian Holt.
* AI (Claude) only used for:

  * Generating sample data (SQLite).
  * SEO content (summaries/keywords).
* Stance: AI is powerful if you understand the code and review it like an intern’s work; risky if relied on without depth.

## React 19 Notes

* React 19 recently released after long testing (used internally by Facebook for \~2 years).
* Stable despite being “new.”
* Major feature: React Server Components (RSCs).
* Other new features (like React Compiler) covered in **Complete Intro to React v9**, not this course.
* Course focuses primarily on RSCs and their practical use.

## Render Modes & Server Components

* **Render modes**: Four different ways to write React (not official terms, Brian’s own). They can be mixed, not mutually exclusive.
* **Client-Side React (CSR)**:

  * Traditional SPA approach (10+ years old, still widely used).
  * Ships HTML + JS bundle, browser handles rendering.
  * Server only sends `index.html`.
  * Default starting point for most projects.
* **Server-side features (SSR, SSG, RSCs)**:

  * Optional, not always a win.
  * Should solve a real problem (performance, SEO, etc.).
  * Adds complexity—measure if it’s worth it.
* **Static Site Generation (SSG)**:

  * Pre-renders content to static HTML.
  * Great for marketing/tutorial sites, mostly text/images, minimal interactivity.
  * Example: This course site uses Next.js SSG and is hosted free on GitHub Pages.
  * Markdown → HTML pages workflow.
* **Next.js**:

  * Excellent for hybrid approaches.
  * SSG, SSR, and RSC support out of the box.
  * Brian uses it extensively (Neon, other companies).
* **Setup demo**:

  * `mkdir SSG && cd SSG`
  * `npm init -y`
  * `npm install react@19 react-dom@19`
  * Use **ES modules** (`"type": "module"`) in `package.json`.
  * Skip JSX/Babel to stay simple (focus is Node, not React syntax).
  * Create `index.html` with a `div#root` and special comment placeholder for React render.
