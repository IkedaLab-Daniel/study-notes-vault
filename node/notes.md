## API Design with Node.js V4 
- FrontendMasters | Scott Moss

* Course focuses on **designing APIs in Node.js** with updated tools and techniques.
* No need to have taken V3, though it covers different things.
* Topics covered:

  * Overview of course goals, tools, and what you’ll build.
  * Basics of building a **vanilla Node.js API** (no framework).
  * Anatomy of an API and its components.
  * Using **Express** to simplify API development.
  * Using **Prisma** to interact with databases.
  * **Data modeling**: schema design from real-world ideas.
  * **Routes and middleware**: designing interaction patterns.
  * **Authentication, authorization, identification** explained and implemented.
  * **Route handlers**: core logic connecting clients to the database.
  * **Error handling** to keep APIs stable and resilient.
  * **Configuration with environment variables** for flexibility.
  * **Performance techniques** to keep APIs fast in Node.js.
  * **Testing** to ensure functionality and reliability.
  * **Deployment** so APIs can be used and connected to apps.

## Tools Used in API Design with Node.js V4

* **Runtime**:

  * **Node.js** – JavaScript runtime outside the browser.
  * Chosen because: familiar for frontend devs, large ecosystem, widely used.

* **Framework**:

  * **Express.js** – most popular Node.js framework for APIs.
  * Large community, foundational for many other frameworks, and instructor’s preferred choice.

* **Database**:

  * **Postgres** – replacing MongoDB used in earlier versions.
  * Instructor has recent experience with it, widely adopted, strong SQL ecosystem, good career skill.

* **Hosting**:

  * **Render.com** – modern platform with simple Node.js deployment, similar to early Heroku experience.
  * Will discuss alternatives but focus is on Render.

* **Project**:

  * Building a **changelog app** where users can post product updates/features.

* **Language/Modules**:

  * Start with **CommonJS (require)**, then switch to **ES6 modules (import/export)**.
  * **TypeScript** will be added later for typing and better structure.

## Building a Vanilla Node.js API

We begin by creating a basic API in Node.js without any framework. A new NPM project is initialized, and a simple server is built using Node’s built-in `http` module. This module allows handling requests and responses directly, forming the foundation of how frameworks like Express work.

The server listens for incoming requests, checks the request method (`GET`, `POST`, etc.) and URL, and responds accordingly. A simple router logic is created to handle requests to the root path (`/`). The response is closed using `res.end()`.

The server is started using `server.listen()` on port `3001`, and a message is logged to confirm it’s running. Unlike regular scripts, the server stays active, waiting for requests. Testing in the browser shows the request flow: the browser sends a `GET` request, the server handles it, logs a message in the terminal, and ends the response.

This demonstrates the fundamentals of how an API server works:

* A client sends a request.
* The server processes it.
* The server sends back a response.

Every API you’ll build follows this same request–response cycle, with additional complexity for routing, data handling, and features.

## Why Not Build APIs Without a Framework?

Writing APIs directly with Node’s `http` module is fine for small or trivial projects, or in constrained environments like serverless functions where size matters. But for real-world apps or team projects, this approach quickly breaks down:

* **Lack of Structure** – Without a framework, every developer may implement routing and request handling differently, leading to chaos.
* **Reinventing the Wheel** – Handling routing, parsing, validation, error handling, and more eventually means you’re building your own framework.
* **Team Collaboration Issues** – On larger teams, inconsistent patterns slow development and maintenance.

The `http` module gives powerful request (`req`) and response (`res`) objects.

* `req` contains details about the client’s request (method, URL, headers, IP, body, etc.) and can be logged or inspected.
* `res` is used to send responses back, scoped to the specific request that triggered it.

This is event-driven: a request acts like an event, and the callback is the event handler, similar to `addEventListener` in the browser.

Finally, requests don’t show under **XHR** in DevTools unless explicitly made via JavaScript (`fetch`/`XHR`). Typing a URL in the browser is just a normal `GET` request for a document. Since we didn’t return HTML or data, the browser just shows a blank page, though the request is visible under the **Network tab**.

## Core Parts of Every API

APIs, regardless of language or framework, share common building blocks:

### 1. **Server**

* A server is an application that runs continuously without a visual interface.
* It listens for requests from clients (web apps, mobile apps, other services) and responds.
* Typically sits in front of a database and acts as the gatekeeper (like a bouncer at a club).
* Servers must run on a **port** (a unique number identifying a service on a machine).
* Each server also has an **IP address** (like a home address), which ensures uniqueness across a network.

Example:

```
http://127.0.0.1:3001
```

* `127.0.0.1` → IP address (localhost)
* `3001` → port

### 2. **Routes**

* A route = **HTTP method + URL path**.
* Defines what action to take when a request is received.
* Example routes:

  * `GET /api/user/1` → retrieve user info
  * `POST /api/food` → create a new food record

### 3. **HTTP Methods**

* **GET** → retrieve data
* **POST** → create new data
* **PUT** → replace existing data
* **PATCH** → update part of existing data
* **DELETE** → remove data
* **OPTIONS** → used internally for CORS checks

### 4. **Route Handlers**

* Functions that run when a request matches a route.
* Comparable to event handlers in the frontend (e.g., `onclick`).
* This is where the server interacts with databases, performs logic, and returns a response.

### 5. **Design Patterns**

* While developers can technically do anything with methods/routes, agreed patterns bring consistency.
* The most common is **REST** (Representational State Transfer).
* Alternatives include **GraphQL**, **gRPC**, and **Protobuf**.

## Express.js Basics

* **What is Express?**

  * The most popular Node.js framework for building APIs.
  * Built on top of the now-defunct Connect library.
  * Similar to Django (Python), Sinatra (Ruby), Spring (Java), Gin (Go).
  * Lightweight, respected, widely adopted, and not going away.

* **Installing & Setting Up Express**

  ```bash
  npm i express --save
  ```

  * Create `server.js`.
  * Import and initialize Express:

    ```js
    const express = require("express");
    const app = express();
    ```
  * Define a route:

    ```js
    app.get("/", (req, res) => {
      res.status(200).json({ message: "hello" });
    });
    ```
  * Export app:

    ```js
    module.exports = app;
    ```
  * In `index.js`:

    ```js
    const app = require("./server");
    app.listen(3001, () => console.log("Server running on port 3001"));
    ```

* **Status Codes**

  * `200–299` → success
  * `400–499` → client errors (e.g., bad input)
  * `500–599` → server errors (e.g., crash, DB issues)
  * Respecting status codes helps browsers, tools, and clients interpret responses correctly.

* **Responses with Express**

  * Can send back JSON, text, HTML, images, or any file/data type.
  * Example:

    ```js
    res.send("Hello World");     // plain text
    res.json({ msg: "Hello" }); // JSON
    res.sendFile("/path/to/file.html"); // file
    ```

* **Why Express Helps**

  * Replaces messy `if` statements for routing with clean, declarative methods.
  * Handles HTTP methods and paths without manually writing logic.
  * Provides helpful utilities on `req` and `res` objects.

## ORMs and Databases

* **What is a Database?**

  * Mechanism to persist data on disk (SSD/HDD).
  * Unlike code (in RAM, temporary), databases store data permanently.
  * Many types exist (SQL, NoSQL, etc.).

* **What is an ORM?**

  * **Object-Relational Mapper** = SDK for your database.
  * Lets you interact with a database using functions instead of raw SQL queries.
  * Example:

    ```sql
    INSERT INTO customers (name, email) VALUES ('Alice', 'alice@mail.com');
    ```

    With ORM:

    ```js
    Customer.create({ name: "Alice", email: "alice@mail.com" });
    ```
  * Provides schemas, models, and abstractions for database operations.
  * Think of it as **OOP for databases**.

* **Why Use ORMs?**

  * Easier to use for devs not fluent in SQL.
  * Cleaner, more maintainable code.
  * Works across multiple database systems with the same API.

* **Postgres vs MongoDB**

  * **Postgres**: Relational, supports JSON storage, strong ACID compliance.
  * **MongoDB**: Document-based, also supports ACID transactions now.
  * Today, the performance and feature differences are negligible for most projects.
  * Choice often comes down to:

    * Developer comfort
    * Ecosystem & tooling
    * Cost and hosting options

Great summary you pulled from Scott’s lesson 👌 Let’s unpack the important parts:

---

## 📌 ORM We’ll Use → **Prisma**

* **Prisma** = modern ORM for Node.js that is:

  * **Database agnostic** → works with Postgres, MySQL, SQLite, Mongo, PlanetScale, etc.
  * **Type-safe** → autocompletes queries based on your schema (thanks to TypeScript).
  * Handles **queries, schema definitions, migrations, and seeding**.

> You can think of Prisma as a **database SDK + schema toolchain** for Node.js.

---

## ⚡ Database Setup

1. **Recommended** → use **Render.com** (free Postgres DB).

   * Just sign up → create PostgreSQL → choose **Free plan** (can’t downgrade later).
   * Copy **external database URL**, not the internal one.
2. **Alternative** → install Postgres locally.

   * Works, but slightly more setup and troubleshooting.

---

## 🛠 Installing Prisma + TypeScript

Since Prisma’s big strength = **type safety**, we need TypeScript in the project.

Run:

```bash
npm install -D typescript ts-node @types/node prisma
```

* `typescript` → compiler (TS → JS).
* `ts-node` → run TypeScript directly without pre-building.
* `@types/node` → type definitions for Node.
* `prisma` → the ORM itself.

---

## ⚙️ Setup TypeScript Config

Create a file at the root → **`tsconfig.json`**

```json
{
  "compilerOptions": {
    "target": "es2020",
    "module": "commonjs",
    "moduleResolution": "node",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "dist"
  },
  "include": ["src"],
  "exclude": ["node_modules"]
}
```

👉 Scott’s advice: **remove `"strict": true`** if you’re new to TypeScript.
Otherwise, you’ll have to write explicit types for everything, which slows you down at first.

---

✅ At this point, you’ve got:

* Postgres (on Render or local).
* Prisma installed.
* TypeScript set up.

Next step will be **Prisma init** (`npx prisma init`) → this creates:

* `prisma/schema.prisma` (your data models).
* `.env` (where you’ll paste the Postgres connection string).

## Designing Models and Writing Prisma Schema

To design database models, Scott looked at a **Figma UI for a changelog app**. The UI helps determine what data the app needs, which informs the schema design.

### Potential Models

* **User** → required for authentication and ownership
* **Roadmap**
* **Projects**
* **Tasks**
* **Features**

### Prisma Syntax Example: `User` Model

Prisma schema syntax is similar to GraphQL/JSON object style. Example:

```prisma
model User {
  id        String   @id @default(uuid())
  username  String   @unique
  password  String
  createdAt DateTime @default(now())
}
```

* `@id` → marks primary key
* `@default(uuid())` → generates a UUID automatically
* `@unique` → ensures unique usernames
* `@default(now())` → sets timestamp when record is created

### Key Notes

* Prisma schema is **database-agnostic** → works the same for Postgres, MySQL, etc.
* Relationships between tables can be defined easily (Prisma VSCode extension helps).
* **UUIDs are preferred** over auto-incrementing integers for safer, globally unique IDs.

## Product, Update, and UpdatePoint Models with Prisma

### Models Breakdown

* **Product** → main entity
* **Update** → belongs to a product, has details like title, body, status, etc.
* **UpdatePoint** → belongs to an update, smaller pieces of info (name + description)

### Prisma Schema Examples

#### Update Model

```prisma
model Update {
  id        String   @id @default(uuid())
  createdAt DateTime @default(now())
  updatedAt DateTime

  title     String
  body      String
  status    UPDATE_STATUS @default(IN_PROGRESS)
  version   String?   // optional
  asset     String?   // optional (e.g., GIF/URL)

  productId String
  product   Product   @relation(fields: [productId], references: [id])

  points    UpdatePoint[]
}

enum UPDATE_STATUS {
  IN_PROGRESS
  SHIPPED
  DEPRECATED
}
```

#### UpdatePoint Model

```prisma
model UpdatePoint {
  id          String   @id @default(uuid())
  createdAt   DateTime @default(now())
  updatedAt   DateTime

  name        String
  description String

  updateId    String
  update      Update @relation(fields: [updateId], references: [id])
}
```

### Key Notes

* `@relation` → sets up relationships between models.
* `?` → makes a field optional (e.g., version, asset).
* `enum` → defines fixed constants like statuses.
* Relationships:

  * **Product → Update → UpdatePoint**
* Prisma auto-updates relations when running `npx prisma format`.

This schema models a real-world changelog app by reflecting design → database structure.

## Prisma Migrations

* **Purpose of Migrations**

  * Teach the relational database about the schema so it can create tables.
  * Handle schema changes (breaking changes) by moving existing data into the new structure (hence "migration").

* **Challenges**

  * Required for relational databases, not for NoSQL.
  * Common source of downtime and issues in production.
  * Prisma simplifies migrations significantly.

* **Prisma Client**

  * ORM / SDK used inside code to talk to the database.
  * Generated automatically after each migration based on the schema.
  * Different schemas → different clients.

* **Setup Steps**

  1. Ensure `.env` has `DATABASE_URL` pointing to your Postgres instance.
  2. Install Prisma Client.
  3. Run initial migration:

     ```bash
     npx prisma migrate dev --name init
     ```
  4. Migration creates:

     * A `migrations/` folder with timestamped SQL files.
     * Updated Prisma Client generated from your schema.

* **Key Benefit**

  * Prisma auto-generates the SQL migration scripts you’d otherwise have to write manually.

## Routes and CRUD in Express

* **CRUD Basics**

  * CRUD = Create, Read, Update, Delete.
  * Almost every app/API centers around these operations on resources (e.g., users, products, updates).

* **REST Approach**

  * Each resource gets routes for CRUD operations.
  * Example for **Product**:

    * `GET /product` → get all products
    * `GET /product/:id` → get one product
    * `POST /product` → create product
    * `PUT /product/:id` → update product
    * `DELETE /product/:id` → delete product
  * Same pattern applies for **Update** and **UpdatePoint** resources.

* **Express Router**

  * `app` = entire API (global).
  * `Router` = sub-app, allows separating routes (e.g., authenticated vs. non-authenticated).
  * Useful for organizing APIs with different middleware/configurations.

* **Route Parameters**

  * `:id` (or any name after `:`) defines a **dynamic parameter**.
  * Example: `GET /product/:id` → access with `req.params.id`.

* **PUT vs PATCH**

  * **PUT**: replaces the entire resource (except `id`).
  * **PATCH**: updates only specific fields provided.
  * Many developers use PUT like PATCH (never fully replace).

* **When to Use gRPC vs REST**

  * **gRPC**: great for internal APIs (your frontend/mobile app consuming your backend).

    * Can fetch all required data in one call.
  * **REST**: better for public/external APIs.

    * More generic, widely supported, predictable.

* **tRPC**

  * Type-safe version of RPC for TypeScript.
  * Provides automatic type inference between backend and frontend.
  * Similar benefit to GraphQL with generated types, but without an extra build step.
  * Still has trade-offs in developer experience.

## Mounting the Router to the App

* The router must be attached back to the main app, otherwise it won’t do anything.
* Export the router (`export default router`) and import it into `server.ts`.
* Routes order matters: if two routes share the same method + path, Express executes the first one registered.
* Use `app.use()` to mount the router:

  * Example: `app.use("/api", router)`
  * This makes all router routes available under `/api/...` (e.g., `/api/product`).
* Routers let you separate and modularize routes like reusable components, making APIs more organized.

## Testing Routes & Handling Responses

* After creating routes, attach them to handlers or else requests will **hang** (server picks up but never responds).
* Use **Thunder Client** (VS Code plugin) to test API requests (GET, POST, PUT, DELETE) without writing frontend code.
* Example: `GET /api/product` → initially hung, fixed by adding a handler:

  ```ts
  router.get("/product", (req, res) => {
    res.json({ message: "hello" });
  });
  ```
* A server must **always respond once**:

  * ❌ Never hang (no response).
  * ❌ Never respond twice (causes errors).
* Tools like **nodemon** can auto-restart the server on file changes (not enabled by default with Node/TypeScript).
* Next step: learn **middleware**, which sits between requests and responses, handling logic before/after route handlers.

### Middleware in Express – Key Takeaways

✅ **What is middleware?**

* Functions that run **before your route handler** executes.
* Each receives `(req, res, next)`

  * `req`, `res` → same as in handlers
  * `next()` → tells Express to move on to the next middleware/handler

✅ **Use cases**

* Logging requests (like Morgan)
* Error handling
* Authentication & authorization
* Request transformations (adding fields, sanitizing, etc.)
* Blocking/short-circuiting requests (e.g., deny certain IPs)

✅ **Flow**

* Middleware stack = array of functions registered in order.
* When you call `next()`, Express moves to the next function in the stack.
* A middleware can also **end the response** itself with `res.send()`, `res.json()`, etc.
* Order **matters** → middleware should be declared *before* routes if it should affect them.

✅ **Global vs Scoped Middleware**

* **Global**:

  ```ts
  app.use(morgan("dev"));
  ```

  Runs for *all* requests.

* **Scoped to a path**:

  ```ts
  app.use("/api", someMiddleware);
  ```

  Runs only for `/api/...` routes.

* **Scoped to a single route**:

  ```ts
  router.get("/product", authMiddleware, (req, res) => {
    res.json({ message: "hello" });
  });
  ```

  Only `/product` calls go through `authMiddleware`.

✅ **Morgan example**

```ts
import express from "express";
import morgan from "morgan";

const app = express();

// global middleware
app.use(morgan("dev"));

// route
app.get("/api/product", (req, res) => {
  res.json({ message: "hello" });
});
```

When you hit `/api/product` →

* Morgan logs request details
* Then handler sends JSON response

### Custom middlewares

* Middleware runs **before** your route handler executes.
* Can:

  * Log requests (`morgan` is a common logger middleware).
  * Parse request bodies (`express.json()` & `express.urlencoded()`).
  * Handle authentication & authorization.
  * Catch and handle errors globally.
  * Augment (`req`) or (`res`) with extra data.
  * Even **short-circuit** the request (send a response early without calling `next()`).

---

### 🔗 Middleware Signature

Every middleware looks like:

```js
(req, res, next) => {
  // do something...
  next(); // pass control to the next middleware/handler
};
```

* If you call `next()`, Express continues to the next middleware or route handler.
* If you **don’t** call `next()` (and instead send a response), the request stops there.

---

### 📚 Built-in Useful Middleware

* **`express.json()`** → Parses JSON body into `req.body`.
* **`express.urlencoded({ extended: true })`** → Parses URL-encoded data (like HTML form submissions).
* **`cors()`** → Handles Cross-Origin Resource Sharing rules.

---

### 🛠 Example with Middleware in Action

```js
import express from "express";
import morgan from "morgan";
import cors from "cors";

const app = express();

// Global middleware
app.use(morgan("dev")); // logs each request
app.use(express.json()); // parses JSON body
app.use(express.urlencoded({ extended: true })); // parses query strings
app.use(cors()); // allows cross-origin requests

// Custom middleware
app.use((req, res, next) => {
  req.secret = "doggy"; // augment request
  console.log("Custom middleware ran ✅");
  next();
});

// Route handler
app.get("/product", (req, res) => {
  res.json({ message: req.secret }); // "doggy"
});

// Example middleware that blocks access
app.use((req, res) => {
  res.status(401).send("Nope!");
});

app.listen(3000, () => console.log("Server running on port 3000"));
```

---

### 🧩 Middleware Options & Composition

* Middleware can be:

  * **Global**: `app.use(middleware)` → runs for every request.
  * **Route-specific**: `app.get("/path", middleware, handler)`.
* Can be passed as:

  * **Multiple args**:

    ```js
    app.get("/secure", authMiddleware, logMiddleware, handler);
    ```
  * **An array**:

    ```js
    app.get("/secure", [authMiddleware, logMiddleware], handler);
    ```

---

### 🕸 Answer to your classmate’s questions

1. **What if you call `next()` inside a handler?**

   * It doesn’t make sense — route handlers are “end of the line.”
   * Express will try to look for *another matching handler*, but if there’s none → request hangs.

2. **Can middleware be chained/nested?**

   * Yes. Best practice = **compose them in arrays** or apply them in order per route.

---

✅ In short: Middleware = building blocks to preprocess requests and control flow in Express.

## Authentication: CORS vs Auth

* **CORS**: browser-level protection → checks “can this client even *talk* to me?”
  (like a bouncer checking *if you’re on the list to enter the building*).
* **Authentication**: once you’re in, *who are you?*
* **Authorization**: once we know who you are, *what are you allowed to do?*

---

## 🔐 JWT (JSON Web Token) Basics

A JWT is just:

1. **Payload (data about the user)** → usually minimal, e.g. `id`, `username`, maybe `role`.
2. **Signed with a secret** → so the server can trust it wasn’t tampered with.
3. Stored **client-side** (cookie or localStorage) and sent with every request (usually in the `Authorization` header as `Bearer <token>`).

Example structure:

```
Header.Payload.Signature
```

Decoded payload might look like:

```json
{
  "id": 123,
  "username": "tetey"
}
```

---

## 📦 Installing Dependencies

```bash
npm install jsonwebtoken bcrypt dotenv
```

> ⚠️ `bcrypt` sometimes fails on Apple M1/Intel. If so, use [`bcryptjs`](https://www.npmjs.com/package/bcryptjs) — same API, pure JS.

---

## 🗂 Project Structure (your approach is solid 👍)

```
src/
 ├── index.ts         # Entry (dotenv.config here)
 ├── modules/
 │    └── auth.ts     # JWT utils, auth middleware, hashing
```

---

## ✨ Example `auth.ts`

Here’s what that file could look like:

```ts
import jwt from "jsonwebtoken";
import bcrypt from "bcrypt";

const JWT_SECRET = process.env.JWT_SECRET || "default_secret";

// Create a JWT for a user
export function createJWT(user: { id: number; username: string }) {
  return jwt.sign(
    { id: user.id, username: user.username },
    JWT_SECRET,
    { expiresIn: "1h" } // optional expiration
  );
}

// Verify a JWT (middleware will use this)
export function verifyJWT(token: string) {
  return jwt.verify(token, JWT_SECRET);
}

// Hash password
export async function hashPassword(password: string) {
  const salt = await bcrypt.genSalt(10);
  return bcrypt.hash(password, salt);
}

// Compare password with stored hash
export async function comparePasswords(password: string, hash: string) {
  return bcrypt.compare(password, hash);
}
```

---

## ⚡ Middleware for Protecting Routes

```ts
import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";

const JWT_SECRET = process.env.JWT_SECRET || "default_secret";

export function protect(req: Request, res: Response, next: NextFunction) {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    return res.status(401).json({ message: "Not authorized" });
  }

  const token = authHeader.split(" ")[1];
  try {
    const user = jwt.verify(token, JWT_SECRET);
    // Attach decoded user to req for later
    (req as any).user = user;
    next();
  } catch (err) {
    return res.status(401).json({ message: "Invalid token" });
  }
}
```

Usage in your routes:

```ts
import { protect } from "./modules/auth";

app.get("/products", protect, (req, res) => {
  const user = (req as any).user; // id + username from JWT
  res.json({ message: `Hello ${user.username}` });
});
```

---

## 🍪 Where to Store the Token?

* **Cookies (httpOnly, secure)** → best for browser apps (auto-sent with every request).
* **LocalStorage** → easier to demo but riskier (susceptible to XSS).
* Either way → server always checks `Authorization: Bearer <token>` header.

---

✅ So the flow will be:

1. User signs up → password hashed → stored in DB.
2. User logs in → password compared → JWT created + sent back.
3. Client stores token (cookie or localStorage).
4. Every request includes JWT in header → server verifies → request allowed or denied.

### Protecting Routes

```ts
// src/modules/auth.ts
import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";

const JWT_SECRET = process.env.JWT_SECRET || "default_secret";

// Middleware to protect routes
export function protect(req: Request, res: Response, next: NextFunction) {
  const bearer = req.headers.authorization;

  // 1. No token at all
  if (!bearer) {
    return res.status(401).json({ message: "Not authorized, no token" });
  }

  // 2. Must start with "Bearer "
  if (!bearer.startsWith("Bearer ")) {
    return res.status(401).json({ message: "Not authorized, invalid format" });
  }

  const token = bearer.split(" ")[1].trim();

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    // attach user payload to request for later use
    (req as any).user = decoded;
    next(); // go to next handler
  } catch (err) {
    return res.status(401).json({ message: "Not authorized, invalid token" });
  }
}
```

Then in your server (e.g. `server.ts` or `index.ts`):

```ts
import express from "express";
import { protect } from "./modules/auth";
import productRouter from "./routes/product"; // example

const app = express();

app.use(express.json());

// Protect everything under /api
app.use("/api", protect, productRouter);

app.listen(3000, () => console.log("Server running on port 3000"));
```

---

🔑 Flow when you test:

1. **No `Authorization` header** → `401 Not authorized, no token`.
2. **Wrong format (not `Bearer ...`)** → `401 Not authorized, invalid format`.
3. **Expired/invalid token** → `401 Not authorized, invalid token`.
4. **Valid token** → request goes through, and `req.user` will hold the decoded payload.

## Protect Middleware with JWT Verification

* Middleware ensures only authenticated users can access protected routes.

* Steps:

  1. **Check for Authorization header** → must exist.
  2. **Check format** → must start with `"Bearer "` and include a token.
  3. **Verify token** → use `jwt.verify(token, process.env.JWT_SECRET)` inside a `try/catch`.
  4. **On success** → attach decoded user payload to `req.user` and call `next()`.
  5. **On failure** → return `401 Unauthorized` with a message.

* Example flow:

  * No header → `401 Not authorized, no token`.
  * Wrong format → `401 Not authorized, invalid format`.
  * Invalid/spoofed token → `401 Not authorized, invalid token`.
  * Valid token → request continues, handlers can access `req.user` (with `id` and `username`).

* `try/catch` prevents invalid tokens from crashing the server. Without it, `jwt.verify` errors could shut down the app.

* **Rate limiting**:

  * Can be implemented as middleware but is more efficient at the network layer (e.g., proxy, API gateway).
  * Protects against abuse like bots flooding requests.

* ✅ Result: Routes under `/api` are now guarded — only valid JWT holders can access database endpoints.
