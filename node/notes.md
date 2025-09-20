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
