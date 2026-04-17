## Course Overview

* Introduction to Next.js, a React-based framework for building fast, scalable web applications
* Covers fundamentals: project setup, page creation, data fetching, and styling
* Focus on hands-on learning to build dynamic, high-performance apps
* Prepares learners for more advanced Next.js topics

## Target Learners

* Beginner web developers
* React developers wanting deeper knowledge
* Software engineers exploring modern frameworks
* IT professionals integrating Next.js into projects
* Students and aspiring developers interested in dynamic web apps

## Prerequisites

* Basic knowledge of HTML, CSS, and JavaScript
* React knowledge is helpful but not required
* Willingness to learn and build projects

## Lessons Description

### Getting Started with Next.js

* Install and set up a Next.js project
* Create pages
* Run the development server

### Core Concepts of Next.js

* Routing system
* Data fetching methods
* Component styling

### Enhancing Your Next.js App

* Navigation between pages
* Environment variables for configuration and security

## Learning Outcomes

* Evaluate Next.js compared to other frameworks
* Build production-ready apps using routing, data fetching, and styling
* Apply advanced features like navigation and environment configuration
* Develop a roadmap for improving Next.js skills through projects

## Tips for Learners

* Experiment with different setups and styles
* Use official documentation as a reference
* Engage in discussions to learn from others
* Practice by building projects (e.g., a blog app)

# Introduction and Welcome

* Modern web apps must be fast and optimized, especially for mobile (over 60% of traffic comes from mobile devices)
* Poor performance leads to high bounce rates, abandoned carts, and lower search rankings

## Why Next.js

* A React-based framework focused on speed, performance, and SEO
* Transforms slow, inefficient websites into fast, optimized applications
* Key advantage: improves both user experience and search engine visibility

## What You Will Learn

* Server-Side Rendering (SSR)
* Static Site Generation (SSG)
* Efficient routing system
* Creating dynamic pages
* Data management and performance optimization

## Course Approach

* Start with project setup and basics
* Progress to building dynamic and scalable applications
* Focus on real-world performance improvements

## Goal

* Build high-performance, scalable, and SEO-friendly web applications
* Gain skills to stay competitive in modern web development

## Why Next.js Matters

* Next.js improves performance, scalability, and flexibility
* Can transform slow websites into fast, optimized applications
* Used by companies like Twitch, Netflix, and Hulu

## Server-Side Rendering (SSR)

* Renders content on the server instead of the browser
* Results in faster load times
* Improves SEO and overall performance

## Static Site Generation (SSG)

* Generates static HTML pages in advance
* Ideal for blogs or portfolios with less frequent updates
* Provides very fast loading speed

## File-Based Routing

* Routing is based on file structure
* Creating a file in the `pages` folder automatically creates a route
* Simpler and faster than configuring routing libraries manually

## Automatic Code Splitting

* Splits code into smaller bundles per page
* Loads only necessary JavaScript
* Improves performance and user experience

## SEO Benefits

* Server-side rendering allows search engines to easily crawl pages
* Helps improve search engine rankings compared to traditional React apps

## Built-in API Routes

* Create backend APIs directly inside a Next.js project
* No need for a separate server (e.g., Express)
* Simplifies full-stack development

## Key Takeaway

* Next.js simplifies development while improving performance
* Provides built-in features that make React apps faster, scalable, and SEO-friendly

# Setting Up Next.js

* Setting up a Next.js project is fast and beginner-friendly
* Requires Node.js to run JavaScript outside the browser
* Use any code editor (e.g., VS Code)

## Install Node.js

* Download from official website
* Choose correct version for your OS
* Verify installation using:

  * `node -v`

## Create Next.js Project

* Open terminal in your project folder
* Run command:

  * `npx create-next-app@latest`
* Configure setup options:

  * Project name
  * TypeScript (optional)
  * ESLint (recommended)
  * Tailwind CSS (optional)
  * App Router (recommended)

## Verify Installation

* Check Next.js version:

  * `npx next -v`
* Confirms successful setup

## Project Structure Overview

* `app/` → main application folder
* `page.js` → main page component
* `layout.js` → layout structure
* `node_modules/` → dependencies

## Run the Development Server

* Navigate to project folder:

  * `cd project-name`
* Start app:

  * `npm run dev`
* Runs on:

  * `http://localhost:3000` (default)

## Making First Changes

* Edit `app/page.js`
* Modify content (e.g., create "Hello World")
* Changes auto-update in browser (hot reload)

## Key Takeaways

* Next.js setup is quick and simple
* Built-in tools reduce configuration effort
* Automatic reload speeds up development
* Ready to start building pages immediately

# Creating Your First Page in Next.js

* Pages are created using the `app` directory
* `page.js` inside `app/` is the root (homepage)
* Each new page is created by adding a folder with a `page.js` file

## File-Based Routing Example

* Create folder: `app/about/`
* Add file: `app/about/page.js`
* Automatically creates route:

  * `/about`
* No manual routing configuration needed

## Basic Page Example

* Export a function that returns JSX
* Example: display a simple heading like "About Us"

## Navigation Between Pages

* Use built-in `Link` component
* Add link in homepage (e.g., "Go to About Page")
* Enables seamless navigation

## Client-Side Navigation

* No full page reload when navigating
* Only necessary parts of the page are updated
* Results in faster and smoother user experience

## Key Concept

* Next.js combines:

  * Server-Side Rendering (initial load)
  * Client-Side Navigation (fast transitions)

## Key Takeaways

* Creating pages is simple with file-based routing
* Navigation is optimized and fast
* Easy to build multi-page applications without extra setup

# Dynamic Routing in Next.js

* Allows pages to change based on URL parameters
* Useful for dynamic content like blog posts, products, or user profiles
* No complex configuration required

## Creating Dynamic Routes

* Create folder structure:

  * `app/posts/[id]/page.js`
* Square brackets `[id]` define a dynamic parameter
* Automatically creates routes like:

  * `/posts/1`
  * `/posts/2`

## Accessing Route Parameters

* Use `params` inside the component
* Example:

  * `params.id` gives the dynamic value from the URL
* Enables rendering content based on the ID

## Behavior of Dynamic Routes

* Visiting `/posts` → returns 404 (missing parameter)
* Visiting `/posts/1` → displays content for ID 1
* URL changes dynamically update the page content

## Navigation with Dynamic Routes

* Use `Link` component to navigate
* Example links:

  * `/posts/1`
  * `/posts/2`
* Works seamlessly with client-side navigation

## Use Cases

* Blog post pages
* Product detail pages
* User profiles
* Any data-driven page with unique identifiers

## Key Takeaways

* Dynamic routing is simple using file-based structure
* Square brackets (`[param]`) define dynamic segments
* No need for manual routing setup
* Easily scalable for real-world applications

# Data Fetching in Next.js

* Data makes applications dynamic and functional
* Next.js allows fetching data based on routes (e.g., blog posts by ID)
* Enables building real-world, data-driven applications

## Setting Up Mock Data

* Create folder: `app/data/`
* Create file: `posts.js`
* Store mock data (e.g., array of posts with `id`, `title`, `content`)
* Simulates real API or database data

## Fetching Data in Dynamic Routes

* Import data into dynamic route page (`app/posts/[id]/page.js`)
* Use `params.id` to find matching post
* Render post details (title and content) dynamically

## Rendering Dynamic Content

* Each URL (e.g., `/posts/1`) displays specific post data
* Content changes based on route parameter
* Mimics real-world applications like blogs or product pages

## Error Handling

* Check if post exists
* If not found, display message (e.g., "Post not found")
* Important for handling invalid user input or missing data

## Testing the Setup

* `/posts/1` → shows first post
* `/posts/2` → shows second post
* `/posts/3` → shows error message

## Key Takeaways

* Data fetching connects dynamic routes to real content
* Easy to simulate APIs with local data
* Scalable for real backend integration
* Essential for building dynamic web applications

# Styling in Next.js

* Styling transforms functional apps into visually polished designs
* Next.js supports multiple styling approaches
* Common methods: CSS Modules and Tailwind CSS

## CSS Modules

* Create scoped CSS for specific components
* Example file:

  * `post.module.css`
* Prevents global style conflicts

### Applying CSS Modules

* Import styles:

  * `import styles from './post.module.css'`
* Use in components:

  * `className={styles.title}`
* Can style elements like:

  * Container (`main`)
  * Title (`h1`)
  * Content (`p`)

## Benefits of CSS Modules

* Scoped styling (no conflicts)
* Clean and maintainable code
* Ideal for component-specific designs

## Tailwind CSS

* Utility-first CSS framework
* Apply styles directly in className
* No need to write custom CSS

### Tailwind Setup

* Config file: `tailwind.config.js`
* Global styles: `globals.css` (includes base, components, utilities)

### Using Tailwind

* Add utility classes directly:

  * Example:

    * `text-xl` → larger text
    * `font-bold` → bold text
    * `m-4` → margin

## Benefits of Tailwind CSS

* Faster UI development
* No need for separate CSS files
* Highly customizable via config

## Key Takeaways

* CSS Modules → best for scoped, custom styles
* Tailwind CSS → best for rapid UI development
* Both can be used together for flexibility
* Helps create clean, professional-looking applications

# Navigation in Next.js

* Good navigation improves user experience and usability
* Helps users move seamlessly across pages
* Essential for dynamic applications

## Creating a Navigation Component

* Create file: `app/navigation.js`
* Define navigation links (e.g., Home, About, Post 1, Post 2)
* Use `Link` component for routing

## Using a Layout Component

* Wrap page content with a layout component
* Layout includes navigation bar + page content
* Makes navigation reusable across pages

## Adding Navigation to Pages

* Import layout/navigation component
* Wrap page content inside layout
* Repeat for all pages (Home, About, Posts)

## Handling Import Paths

* Ensure correct file paths when importing components
* Use relative paths based on folder structure
* Incorrect paths → module not found error

## Styling Navigation

* Can use Tailwind CSS or custom styles
* Example: change colors (e.g., blue → purple)
* Keeps UI consistent and visually appealing

## Benefits of Layout-Based Navigation

* Reusable across all pages
* Consistent design and structure
* Reduces code duplication

## Key Takeaways

* Navigation should be global and accessible
* Layout components simplify reuse
* Next.js App Router makes integration easy
* Improves overall user experience and app flow

# Environment Variables in Next.js

* Used to securely store sensitive data (e.g., API keys, configs)
* Prevents exposing critical information in code
* Essential for real-world applications

## Creating Environment Variables

* Create file in root directory:

  * `.env.local`
* Store variables:

  * `KEY_NAME=value`
* Example:

  * `NEXT_PUBLIC_API_KEY=your_key_here`

## Accessing Environment Variables

* Use:

  * `process.env.KEY_NAME`
* Example:

  * `process.env.NEXT_PUBLIC_API_KEY`
* Can be used across pages and components

## Public vs Private Variables

* `NEXT_PUBLIC_` prefix:

  * Accessible on both client and server
* Without prefix:

  * Server-side only (more secure)

## Usage in Application

* Can be used for:

  * API keys
  * Database URLs
  * Configuration settings
* Typically used in backend logic, not displayed in UI

## Benefits

* Keeps sensitive data secure
* Easy to manage across environments (development, production)
* Improves maintainability and scalability

## Mini Project Recap

### Dynamic Routing

* Created routes using file-based system
* Used dynamic parameters (`[id]`)

### Data Fetching

* Loaded content based on route parameters
* Simulated API using local data

### Styling

* CSS Modules for scoped styles
* Tailwind CSS for rapid UI development

### Navigation

* Built reusable layout with global navigation bar
* Ensured consistent UI across pages

### Environment Variables

* Stored and accessed sensitive data securely
* Used `.env.local` for configuration

## Key Takeaways

* Environment variables are critical for security
* Next.js simplifies secure configuration management
* Combined features enable building full modern web apps
* Covers core fundamentals of Next.js development
