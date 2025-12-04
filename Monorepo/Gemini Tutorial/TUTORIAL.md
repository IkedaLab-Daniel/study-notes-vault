This tutorial will guide you through building a **TypeScript Monorepo** from scratch using **pnpm workspaces** and **Turborepo**.

This is currently the industry-standard "modern stack" for monorepos because it is fast, space-efficient, and handles caching automatically.

### **What we are building**

  * **Apps:** A web application (React/Next.js) and an API (Node/Express).
  * **Packages:** A shared UI library and shared utility functions.
  * **Tooling:** One command to run them all.

-----

### **Prerequisites**

  * Node.js installed (v18+ recommended).
  * `pnpm` installed (`npm install -g pnpm`).

-----

### **Step 1: Scaffolding the Project**

First, create a directory and initialize the root package.

```bash
mkdir my-monorepo
cd my-monorepo
pnpm init
```

#### **Configure pnpm Workspaces**

Create a file named `pnpm-workspace.yaml` in the root. This tells pnpm where your projects live.

```yaml
# pnpm-workspace.yaml
packages:
  - "apps/*"
  - "packages/*"
```

#### **Root TypeScript Config**

Create a `tsconfig.base.json` in the root. Your apps will "extend" this so you don't have to copy-paste config rules everywhere.

```json
// tsconfig.base.json
{
  "compilerOptions": {
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node",
    "declaration": true,
    "composite": true // Helps with build caching
  }
}
```

-----

### **Step 2: Creating a Shared Package**

Let's create a utility library that both our API and Web App can use.

1.  Create the folder: `mkdir -p packages/utils`
2.  Initialize it: `cd packages/utils && pnpm init`

Update `packages/utils/package.json`. **Crucial:** Change the name to be scoped (e.g., `@repo/utils`).

```json
// packages/utils/package.json
{
  "name": "@repo/utils",
  "version": "1.0.0",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "scripts": {
    "build": "tsc"
  },
  "devDependencies": {
    "typescript": "^5.0.0"
  }
}
```

Create a `tsconfig.json` in this folder:

```json
// packages/utils/tsconfig.json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src"]
}
```

Create the code `src/index.ts`:

```typescript
// packages/utils/src/index.ts
export const capitalize = (str: string) => {
  return str.charAt(0).toUpperCase() + str.slice(1);
};

export const DATE_FORMAT = "YYYY-MM-DD";
```

**Build the package:**

```bash
pnpm build
```

-----

### **Step 3: Creating the Frontend App**

Go back to root (`cd ../../`) and create a React app inside `apps/`. We will use Vite for speed.

```bash
cd apps
pnpm create vite web --template react-ts
cd web
pnpm install
```

#### **Connect the Shared Package**

We need to tell the Web app to use our `@repo/utils`.

In `apps/web/package.json`, add the dependency. Notice the version is `workspace:*`. This tells pnpm "always use the version currently inside this repo."

```json
// apps/web/package.json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "@repo/utils": "workspace:*"  <-- ADD THIS
  }
}
```

Run `pnpm install` in the root to link them.

Now, use it in `apps/web/src/App.tsx`:

```tsx
import { capitalize } from '@repo/utils';

function App() {
  return (
    <div>
      <h1>{capitalize("hello world from the monorepo!")}</h1>
    </div>
  )
}
export default App;
```

-----

### **Step 4: Adding Turborepo (The Orchestrator)**

Right now, you have to go into every folder to run `build` or `dev`. Turborepo solves this.

Install Turbo globally and in the root:

```bash
npm install turbo --global
pnpm add turbo -D -w
```

Create a `turbo.json` in the **root** directory. This defines how tasks relate to each other.

```json
// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      // "dependsOn": ["^build"] means: Build my dependencies first!
      // If Web depends on Utils, build Utils before Web.
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "build/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "lint": {}
  }
}
```

Add these scripts to your **root** `package.json`:

```json
// package.json (root)
{
  "scripts": {
    "dev": "turbo dev",
    "build": "turbo build",
    "lint": "turbo lint"
  }
}
```

-----

### **Step 5: Running the Monorepo**

You can now control the entire universe from the root folder.

**1. Build everything in proper order:**

```bash
pnpm build
```

*Turbo will see that `web` depends on `@repo/utils`. It will build utils first, then build web.*

**2. Run everything in Dev mode:**

```bash
pnpm dev
```

*This will start up your React app, and if you had a backend API in `apps/api`, it would start that simultaneously.*

-----

### **Summary of the Structure**

Your final folder structure should look like this:

```text
my-monorepo/
├── package.json          (Root scripts: turbo build/dev)
├── pnpm-workspace.yaml   (Defines location of apps/packages)
├── turbo.json            (Task pipeline config)
├── tsconfig.base.json    (Shared TS config)
├── apps/
│   └── web/              (React App)
│       ├── package.json  (Depends on "@repo/utils": "workspace:*")
│       └── src/
└── packages/
    └── utils/            (Shared Logic)
        ├── package.json  (Named "@repo/utils")
        ├── tsconfig.json (Extends base)
        └── src/
```

### **Why this is powerful**

1.  **Shared Logic:** If you find a bug in `capitalize`, you fix it in `packages/utils`, and every app gets the fix immediately.
2.  **Shared Types:** You can share TypeScript interfaces between your Backend and Frontend perfectly.
3.  **Caching:** If you run `pnpm build` twice, the second time will be instant because Turbo caches the result.

-----