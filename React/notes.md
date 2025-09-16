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

## Static Site Generation with React (No JSX)

* **App.js setup**

  * Import `createElement` as `h` (old convention, avoids JSX).
  * Define `App` function returning elements:

    * `div` → `h1` (“Hello Frontend Masters”) + `p` (“This is SSG”).
  * `export default App`.
  * Simpler than JSX—no Babel/Vite/Webpack needed.

* **Build.js process**

  * Import `renderToStaticMarkup` from `react-dom/server`.
  * Import `h` (createElement) + `App`.
  * Import Node modules: `fs`, `path`, `url` helpers.
  * Handle `__dirname` workaround for ES modules (`fileURLToPath`).
  * Read `index.html` shell file.
  * Render `App` → string with `renderToStaticMarkup`.
  * Replace placeholder in `index.html` with rendered string.
  * Ensure `dist/` exists:

    * If not → create it.
    * If yes → empty it, then write new `index.html`.

* **Result**

  * Running `node build` generates static HTML in `dist/`.
  * No React reference in output—just plain HTML.
  * This is the essence of **Static Site Generation (SSG)**.

* **Takeaways**

  * Frameworks like Next.js, Astro, Gatsby automate this process.
  * Custom code shows the *first principles* of SSG.
  * Great for content-driven sites (docs, tutorials, marketing).
  * Can still add React interactivity on top (SPA feel, routers).
  * Markdown → HTML → React components possible (e.g., **MDX**).

* **State of the art**:

  * **Next.js** + **Astro** are leading tools today.
  * Gatsby less maintained after Netlify acquisition.

## 🔑 What SSR Does

* Normally (CSR – client-side rendering):

  * Browser requests → server returns empty `index.html` + React bundle.
  * Browser parses + executes React JS → only then app appears & becomes interactive.
  * **Time to first paint = Time to interactive**.

* With **SSR**:

  * Server pre-renders the React component tree → sends HTML markup.
  * Browser shows HTML immediately (fast **first paint**).
  * Then React JS bundle arrives, hydrates, and makes it interactive.
  * **Perceived performance improves** → users see something sooner.

---

## ⚖️ Tradeoffs

* **Pros**

  * Faster perceived load, especially on **slow devices or bad networks**.
  * Useful for rural areas, low-end Android, poor connectivity (e.g., crop trackers, gov apps).
  * SEO benefits (search engines can crawl content directly).

* **Cons**

  * **Slower “time to interactive”** (hydration takes time).
  * **Complexity**:

    * Must handle server + client rendering differences.
    * Browser-only APIs (`window`, `document`, `localStorage`, analytics, etc.) can crash if used during SSR.
  * **Server load**: rendering on the server consumes CPU.
  * Sometimes **worse performance** (e.g., Netflix found SSR harmed certain regions).

---

## 📊 When to Use

* Don’t assume SSR is always a win → **measure it**.

* Tools:

  * **Lighthouse** (first meaningful paint, time to interactive).
  * **Chrome DevTools performance tab**.
  * **Google Analytics** (real user timings).
  * Server instrumentation (Fastify/Express plugins for response timings).

* If your audience:

  * **Fast devices + fast network** → SSR may be useless/slower.
  * **Slow devices + bad networks** → SSR can be a huge UX win.

---

## 🛠️ Implementation Notes

* Typical stack: React + Node server (Fastify, Express, etc.).
* Server sends **pre-rendered HTML** + JS bundle.
* React hydrates → attaches event listeners, enables interactivity.
* Real-world frameworks (Next.js, Remix, Astro) automate this.

---

👉 **Bottom line**:
SSR ≠ universally better. It’s a **tradeoff between complexity and user experience**. Always measure with real-world conditions before committing.

## Writing SSR by Hand

* Created a new directory `SSR` and initialized it with `npm init -y`.
* Installed dependencies: `fastify`, `react`, `react-dom`, and `vite`.
* Recommended locking versions by copying his `package.json` to avoid version drift issues.
* Added scripts in `package.json`:

  * `build`: runs `vite build`.
  * `start`: runs `node server.js`.
  * Also included `"type": "module"`.
* Built a simple `index.html` with a `div#root` as the mount point.
* Warned that **SSR + client hydration is highly sensitive to whitespace**, which can cause hydration errors.
* Explained hydration: server generates markup → client re-checks with a hash → mismatch causes React to discard SSR and re-render, losing SSR benefits.
* Created `app.js` without JSX (using `React.createElement` syntax):

  * Defined a simple `App` component with `useState` to show interactivity.
  * Rendered `h1`, `p`, and a `button` that increments a counter.
* Highlighted how tedious non-JSX code is, making JSX more appreciated.

## Client and Server Setup for SSR

* **Client Setup (`client.js`)**

  * Created `client.js` to handle hydration on the browser.
  * Used `hydrateRoot` instead of `createRoot` to attach React to existing server-rendered markup.
  * Imported `createElement` and the `App` component.
  * Called `hydrateRoot(document.getElementById("root"), h(App))`.
  * Safe place to add browser-only logic (e.g., Google Analytics), since this code never runs on the server.

* **Server Setup (`server.js`)**

  * Imported dependencies: `fastify`, `fastify-static`, `fs`, `path`, `fileURLToPath`, `renderToString`, and `App`.
  * Used `renderToString` (not `renderToStaticMarkup`) to include React metadata for hydration.
  * Read `dist/index.html` as a shell and split it at the `ROOT` placeholder.
  * On `GET /`:

    * Flushed the **head part** (`parts[0]`) first so the browser can start downloading CSS/JS while React renders.
    * Rendered the app with `renderToString(h(App))` and streamed it.
    * Flushed the closing part (`parts[1]`) and ended the response.
  * Registered `fastify-static` to serve built files.
  * Added a `<script type="module" async defer src="./client.js">` in `index.html` to load the client bundle.

* **Build & Run**

  * Needed `vite build` so that the correct hashed script files exist in `dist/`.
  * Then started server with `npm run start`.
  * Verified SSR by checking **View Page Source**, which showed complete markup before React hydration.

* **Key Notes**

  * SSR improves perceived performance by sending usable markup immediately.
  * Hydration errors are often caused by **whitespace mismatches** between server and client render.
  * Frameworks usually handle this automatically, but writing SSR by hand highlights how sensitive it is.

## SSR Questions and Answers

* **Whitespace & Prettier Issues**

  * Hydration errors only matter in `index.html`.
  * Extra whitespace in `index.html` can break hydration because React compares hashes of server vs. client markup.
  * Whitespace in other files doesn’t matter.

* **Changing Counter Start Value**

  * Modify `App` component to set initial state (e.g., `useState(5)`).
  * Since no dev mode is running, changes require:

    1. `npm run build`
    2. Restarting the server

* **Splitting HTML for SSR**

  * `server.js` splits `index.html` at the root div.
  * First part (head + script tags) is sent immediately so browser begins downloading assets.
  * Async + defer attributes are critical so scripts don’t block rendering.
  * Then render React output in the root div.
  * Finally send closing HTML.
  * For multiple “islands” (e.g., micro frontends), split at each root and inject corresponding markup.

* **Render to String vs. Pipeable Stream**

  * `renderToString`: waits until React finishes rendering, then sends one complete chunk.
  * `renderToPipeableStream`: streams chunks as React renders them (e.g., nav first, then body).
  * For small apps, both behave the same. Pipeable streams only help with complex apps needing progressive rendering.
  * If no complexity/size benefits, SSR may not be worth using.

## React Server Components (RSCs)

* **Definition & Difference from SSR**

  * SSR: does one initial render, then client-side React takes over.
  * RSCs: only render on the server, maintaining an ongoing relationship between client and server.
  * They are independent concepts—you can use SSR, RSCs, both, or neither.

* **Key Properties**

  * Client never receives the server component’s code—only markup (or React Flight protocol).
  * Enables writing database queries or using secrets directly inside React components safely.
  * Most of the app’s non-interactive parts can stay on the server, reducing hydration needs.
  * Client bundle shrinks since server components don’t ship to the browser.

* **Benefits & Trade-offs**

  * Less JavaScript downloaded, smaller client bundle.
  * Simplifies workflows (e.g., forms writing directly to DB without separate API endpoints).
  * Great for securely handling API keys/secrets.
  * Downsides: added cognitive load—developers must track “client vs. server” components.
  * Cannot use client-only features (e.g., `useState`) inside RSCs.
  * Performance depends: fewer downloads but more server requests → slow connections may suffer.

* **Framework Support**

  * Next.js: RSCs by default (must opt into client components).
  * TanStack Start: opposite—client by default, opt into server components.
  * React Router v7 & Remix: partial/experimental support.
  * RSCs intended to be used through frameworks, not by hand (unstable APIs).

* **Developer Experience**

  * Shifts paradigm: blends server/client logic, making it feel closer to PHP-style rendering.
  * Allows creating secure, simplified client-server workflows without explicit API layers.
  * Still confusing and evolving—frameworks abstract much of the complexity.

* **Planned Example App**

  * Building a **NotePasser** app (like passing paper notes in class).
  * Simplified for teaching: no authentication (always user ID 1).
  * Auth can be added later with providers like Clerk, Descope, Neon Auth.

## Building RSCs Without a Framework

Brian Holt guided us through setting up React Server Components (RSCs) without using frameworks like Next.js. Instead, we became “the framework,” wiring everything ourselves.

* Started by creating a **new project** with a prepared `package.json` and running `npm install`.
* Used **CommonJS** instead of ES modules to simplify setup.
* Chose **Webpack** (instead of Vite/Parcel) because of the required package `react-server-dom-webpack`, which enables RSC support in Node.
* Added supporting tools: **Babel** (JSX transpiling), **Fastify** (server), **Pino** (logging), **SQLite3** (database), and loaders for **CSS**.
* Configured **webpack.config.js** with:

  * `HtmlWebpackPlugin` to generate the HTML shell.
  * `ReactServerWebpackPlugin` to handle RSC stubs and server actions.
  * Rules for Babel (`.js/.jsx`) and CSS.
  * Output, optimization, and resolve settings.
* Built **babel.config.js** to enable React JSX transform with `"automatic"` runtime.
* Created a minimal **index.html** referencing `index.css` and a `#root` div.
* Added a **notes.db** SQLite file and custom **index.css** inside `public/`.
* Defined scripts in `package.json`:

  * `dev:client` → runs Webpack in watch mode.
  * `dev:server` → runs Node with `--conditions react-server` to ensure proper RSC behavior.

## Creating App, Server, and Client Components

* Created a **`src/App.jsx`** file as the main entry point.

  * Imported `Suspense` from React.
  * Imported `ServerComponent` and `ClientComponent`.
  * Logged render behavior for debugging.
  * Returned a `Suspense` boundary with fallback `"loading"`, plus a header, server component, and client component.
  * By default, components are **server components** unless explicitly marked as client.

* Defined rules:

  * **Server components** → run on the server, cannot use React hooks.
  * **Client components** → required for interactivity and hooks.
  * Server components can contain client components, but not the reverse.

* Built a **client component** (`ClientComponent.jsx`):

  * Added `"use client"` directive at the top.
  * Used `useState` to implement a counter.
  * Returned UI with a counter value and increment button.
  * Confirmed normal React interactivity works in client components.

## Building the Server Component and Client Bootstrap

* **ServerComponent.jsx**

  * Default to server component (no `"use server"` needed).
  * Can use Node APIs (`path`, `sqlite3`) directly.
  * Supports `async/await` in function bodies.
  * Example: `MyNotes` component queries a SQLite `notes.db` file for user notes.
  * Query joins `users` table twice (from\_user, to\_user) to display names instead of IDs.
  * Renders a `<table>` with `from`, `to`, and `note`.
  * Shows how SQL can be written inline within a React server component.
  * **Security note**: escape user-generated content before inserting into DB; React prevents XSS unless using `dangerouslySetInnerHTML`.

* **Database/ORM compatibility**

  * Works with SQLite, Prisma, Drizzle, Neon, etc.
  * Treat server components like API routes—any database logic fits.

* **Client bootstrap (`client.jsx`)**

  * Imports `createRoot` (React DOM) and `createFromFetch` (`react-server-dom-webpack/client`).
  * Loads CSS (`doodle.css`).
  * Fetches markup from `/react-flight` endpoint.
  * `root.render(p)` can directly render the promise returned by `createFromFetch(fetchPromise)`.
  * Allows hydration of server-rendered components into client React tree.

  ## Setting Up the Server with Fastify and React Server Components

* **Main.js (patching requires)**

  * Uses `react-server-dom-webpack/node-register` to patch Node’s require for JSX + React server components.
  * Uses `@babel/register` with plugin `@babel/transform-modules-commonjs` to handle ES modules.
  * Ignores transpiling of `dist`, `server`, and `node_modules` via regex.
  * Runs `require("./server")()` after patching so subsequent requires are processed.
  * Separate file is necessary since patching must happen **before** other requires.

* **Server.js (Fastify server setup)**

  * Requires core modules: `path`, `fs`, `fastify`, `@fastify/static`, `react`, and `react-server-dom-webpack/server`.
  * Loads `App.jsx` as `AppImport.default` (CommonJS interop).
  * Reads **client manifest** (`dist/react-client-manifest.json`) → used as module map for Webpack.
  * Configurable `PORT` via `process.env.PORT` (default 3000).
  * Sets up **Fastify** with `pino-pretty` logger for readable logs.
  * Registers `@fastify/static` twice:

    * Serves `dist` under `/assets`.
    * Serves `public` directly (for CSS, etc.).
  * Route `/` → serves `index.html`.
  * Route `/react-flight` → handler streams React server components using `renderToPipeableStream`.
  * Exports `server` function that starts Fastify and logs errors.
  * Exits with status code `1` on fatal error.

## React Flight Protocol and Streaming with Server Components

* **Manual Flight Protocol (for learning only)**

  * React Flight protocol is essentially **JSON + references** describing UI markup.
  * Uses IDs (`0:`, `$1`, `$L3`, etc.) to reference and reuse components.
  * Mimics `createElement` calls (e.g., `"$":"div"`, children arrays).
  * Not documented publicly, highly unstable—never written by hand in real apps.
  * Example showed raw JSON being interpreted into rendered components.

* **Running the Server with Flight Protocol**

  * Start with `npm run dev:client` to build the client bundle.
  * Then run `npm run dev:server` to serve the app with Flight protocol.
  * Client manifest generated by Webpack provides mapping for bundles and components.
  * Flight protocol responses are transformed by React into actual rendered UI.

* **Switch to Proper Implementation**

  * Removed manual string-based JSON.
  * Used `renderToPipeableStream` from `react-server-dom-webpack/server`.
  * Rendered `React.createElement(App)` with the **module map** from client manifest.
  * Streamed chunks directly with `pipe(reply.raw)` for efficient, incremental rendering.

* **Debugging & Fixes**

  * Adjusted relative paths (e.g., `../`) for correct imports.
  * Resolved missing tables and incorrect manifest file names.
  * Final setup showed:

    * Server component rendering data.
    * Client component handling interactivity.
    * Network tab displaying Flight protocol requests/responses.

  ## RSCs Without vs With Frameworks, and Moving into Next.js

* **Building RSCs Without Frameworks**

  * Possible to build React Server Components (RSCs) entirely from scratch.
  * Demonstrates the inner workings (SQLite backend + client interactivity).
  * Educational, but not practical—frameworks like Next.js make this far easier.

* **Frameworks in Practice**

  * Developers use the same core tools (Webpack, Parcel, Vite, Turbopack).
  * Webpack still widely used, even in large corporations.
  * Turbopack is the “new hotness” and is built into Next.js.
  * Other older tools exist (e.g., Browserify), but modern devs prefer Vite or Parcel.

* **Next.js Context**

  * Next.js is not just a teaching tool, but a production-ready React framework.
  * Built and maintained mainly by Vercel, with many React core contributors.
  * Strong collaboration between Vercel and Meta (Facebook) for React’s evolution.

* **Why Next.js Matters**

  * First widely adopted *full-stack React framework*.
  * Moves more work to the server with **RSC-first architecture**.
  * By default, components are server components—developers must opt into client components.
  * Changes how React apps are written, offering power but also trade-offs.
  * Not every React app needs Next.js; standalone React or other tools (like TanStack Start) remain useful.

* **How Next.js Can Be Used**

  1. **Monolith mode**: Next controls backend, middleware, and frontend (like Rails).
  2. **Middle-end mode**: Next acts as a server that aggregates microservices (e.g., Netflix model), not calling databases directly but consolidating API/service responses.

## Server Components in Next.js with SQLite

* **File Setup**

  * Create `app/my/page.js`.
  * Next.js conventions: lowercase filenames, use `.js` instead of `.jsx`.
  * Case sensitivity issues vary across OS (Linux vs Windows).

* **Database Fetching**

  * Use `sqlite3` with async/await.
  * Define `fetchNotes` function to open `notes.db`.
  * Run two queries (`from` and `to`) in parallel using `Promise.all`.
  * Return both sets of notes.

* **Rendering Notes**

  * Inside `MyNotes`, call `await fetchNotes`.
  * Render notes from the user (“notes from you”) and notes addressed to the user (“notes to you”).
  * Example output includes messages like “Webpack config broke again” and “Your function names are longer than my patience.”

* **Why It’s Simpler in Next.js**

  * Very similar logic to raw RSCs but easier because Next handles boilerplate.
  * Still powered by the **Flight protocol**, just encoded/optimized in the background.
  * Developers focus on queries + markup, not the low-level wiring.

* **Key Insight**

  * Next.js makes React Server Components practical and less error-prone, while still leveraging the same underlying RSC/Flight concepts.

## Writing Notes with Next.js Form Actions

* **Setup**

  * Create `app/write/page.js`.
  * Import `AsyncDatabase` and `postNote` (to be written).
  * Define `getUsers` to query all users from `notes.db`.

* **Why It’s Nice**

  * Next.js lets you run DB queries directly inside React server components.
  * No need for a separate API endpoint or `fetch`; forms can call server functions directly.

* **Form Structure**

  * `<form action={postNote}>` wires the form directly to the server function.
  * Browser manages form state, no need for `useState`.
  * Fields:

    * **From**: `<select name="from_user">` with `users.map` for options.
    * **To**: `<select name="to_user">` (same approach).
    * **Note**: `<textarea name="note" />`.
    * **Submit**: `<button type="submit">`.

* **Key Concept**

  * **Form Actions in Next.js**: form submissions invoke server functions directly with form data.
  * Eliminates boilerplate of extracting values, building API routes, and handling `fetch`.

* **Example Flow**

  * User fills form → submits → Next.js runs `postNote` server function → note saved to database.

## Writing Notes with Server Actions in Next.js

* **PostNote Function**

  * Create `postNote.js`.
  * Must include `"use server"` at the top → ensures it only runs on the server.
  * Function takes `formData`, extracts values with `formData.get("from_user")`, `"to_user"`, `"note"`.
  * Validate inputs → throw error if missing.
  * Save to SQLite DB with parameterized query (`db.run("INSERT INTO notes (from_user, to_user, note) VALUES (?, ?, ?)", [from, to, note])`).

* **Placement**

  * Can live inside `write/page.js` or as its own file.
  * External file requires `"use server"`; inside a server component it’s implicit.

* **Debugging**

  * In **dev mode**, Next.js forwards server errors to the browser (easier debugging).
  * In **production**, errors return as 500s; handle with error boundaries/logging.
  * Standard breakpoints/debugger tools still work.

* **Notes Visibility**

  * “My Notes” page currently filters by `user_id = 1`.
  * Other users’ notes may not appear unless query is adjusted.

* **Under the Hood**

  * Submitting a form with `action={postNote}` → Next.js transparently wires data to the server.
  * Uses built-in protocol (Flight) to send form data; developers don’t need to manage fetch/API endpoints.

* **Limitations**

  * Offline-first apps don’t pair well with RSCs/server actions, since they depend on a server.
  * Would require complex service worker logic for offline handling.

## Mixing Server and Client Components in Next.js

* **Server vs Client Components**

  * Once you enter **client land**, all children are client components.
  * You can’t nest a server component under a client component.
  * Solution: keep server component as parent → pass data down as props.

* **Example: Teacher Feed**

  * **Server Component (`teacher/page.js`)**

    * Imports `fetchNotes` (server function).
    * Loads `initialNotes` via `await fetchNotes()`.
    * Renders `TeacherClientPage` with `initialNotes` + `fetchNotes` passed as props.
  * **Server Function (`fetchNotes.js`)**

    * `"use server"` directive required.
    * Connects to SQLite (`AsyncDatabase.open("./notes.db")`).
    * Returns rows with JOINs to map `from_user` and `to_user`.
    * Optional pagination via `LIMIT`/`OFFSET`.

* **Client Component (`clientPage.js`)**

  * `"use client"` directive required.
  * Uses `useState` for `notes` (initialized with `initialNotes`).
  * Uses `useEffect` with `setInterval` to poll `fetchNotes` every 5s.
  * Appends new notes using spread or `.concat()`.
  * **Cleanup:** `clearInterval` in effect teardown to prevent leaks.
  * Renders teacher’s feed (`ul > li`) with sender, receiver, and note.

* **Polling Behavior**

  * Poll requests may show as `POST` (due to React Flight machinery).
  * Even if a 500 error appears, notes may still update (debug query/columns if broken).

* **Why `"use server"`?**

  * Without it, Next bundles imported server-only libraries (e.g., `sqlite3`) into client bundle.
  * `"use server"` tells Next to exclude it from client-side code.
  * Required for non-component server utilities (actions, functions).
  * Server components imply it automatically, but helper functions need explicit directive.

## Limitations of React Server Components and Workarounds

* **Key Limitation**

  * Server components **cannot** be children of client components.
  * This becomes frustrating when you want to use client state inside a server component (e.g., SQL queries based on client input).
  * In such cases, you must fall back to the **classic approach**:

    * Create an API route.
    * Call it from the client with the necessary parameters.
    * Return results like before RSC existed.

* **Half-Workaround (Children Pattern)**

  * You can pass a **server component as a child** into a client component.
  * Since server components render first (at build or request time), you can pre-render them and let the client component receive them as `children`.
  * This allows server-rendered markup to coexist within client components.

* **Example: WhoAmI Pattern**

  * **Server Component (`WhoAmI.js`)**

    * Fetches user info from database (`AsyncDatabase.open("./notes.db")`).
    * Returns JSX with user details (name + ID).
  * **Client Component (`clientPage.js`)**

    * Accepts `children` (server component) and `id`.
    * Renders the server child

## Key Takeaways on RSCs and Framework Use

* **When to Use Next.js / RSCs**

  * Great for apps where the **client frequently interacts with the server** (lots of API calls, form submissions, database writes).
  * Not ideal for **heavily client-side apps** (e.g., drawing tools like Excalidraw) where state and rendering live almost entirely in the browser.
  * In such cases, lighter setups like **Vite** or **TanStack Router** are better.

* **Rule of Thumb**

  * RSCs are **sometimes useful**.
  * They simplify client-server interaction but can add overhead when the app doesn’t need much server interaction.

* **Other Ecosystems with Similar Paradigms**

  * **Meteor** (JS, older but had seamless client-server data flow).
  * **Rails / Phoenix** (server-driven rendering concepts).
  * **Phoenix LiveView** (Elixir).
  * **Laravel Livewire** (PHP).
  * Similar ideas exist across backends, React just branded it as RSC.

* **Conclusion**

  * React + RSCs aren’t revolutionary but adapt **old server-driven paradigms** for React developers.
  * React’s **flexibility** allows it to work standalone or as the foundation of larger frameworks.
