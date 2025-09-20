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