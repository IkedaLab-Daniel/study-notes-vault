# Monorepo Tutorial

## What is a Monorepo?

A **monorepo** (monolithic repository) is a software development strategy where code for many projects is stored in a single repository. Instead of having separate repos for each package/app, you manage everything together.

### Benefits

✅ **Code Sharing**: Share utility functions, UI components, and types across multiple apps  
✅ **Atomic Changes**: Update shared code and all consumers in a single commit  
✅ **Simplified Dependency Management**: One `node_modules`, consistent versions  
✅ **Better Collaboration**: See the whole system, easier refactoring  
✅ **Unified Tooling**: Single CI/CD pipeline, linting, testing config

### Drawbacks

❌ **Repository Size**: Can grow large over time  
❌ **Build Complexity**: Need smart caching and task orchestration  
❌ **Access Control**: Harder to restrict access to specific packages  

---

## Common Monorepo Tools

| Tool | Description |
|------|-------------|
| **npm workspaces** | Built into npm 7+, simple workspace management |
| **pnpm workspaces** | Fast package manager with efficient disk usage |
| **Yarn workspaces** | Similar to npm workspaces with extra features |
| **Turborepo** | High-performance build system with smart caching |
| **Nx** | Full-featured monorepo tool with code generation |
| **Lerna** | Classic monorepo tool (now maintained by Nx team) |

---

## This Tutorial Structure

We'll build a monorepo using **npm workspaces** with:

```
Monorepo/
├── package.json          # Root config with workspaces
├── packages/
│   ├── utils/           # Shared utility functions
│   └── ui/              # Shared React components
└── apps/
    ├── web/             # React web app
    └── api/             # Express API server
```

### Key Concepts

1. **Workspaces**: Folders managed by the monorepo tool
2. **Internal Dependencies**: Packages reference each other by name
3. **Hoisting**: Shared dependencies are hoisted to root `node_modules`
4. **Task Running**: Build/test packages in correct dependency order

---

## Quick Start

```bash
# Install all dependencies across all workspaces
npm install

# Build all packages (utils, ui) then apps (web, api)
npm run build

# Run the web app (dev mode)
npm run dev:web

# Run the API server
npm run dev:api

# Run tests across all packages
npm test
```

---

## Project Setup Steps

### 1. Initialize Root Package

```bash
npm init -y
```

### 2. Configure Workspaces

Add to root `package.json`:

```json
{
  "workspaces": [
    "packages/*",
    "apps/*"
  ]
}
```

### 3. Create Packages

Each package needs its own `package.json`:

```bash
mkdir -p packages/utils packages/ui apps/web apps/api
```

### 4. Link Internal Dependencies

In `apps/web/package.json`:

```json
{
  "dependencies": {
    "@monorepo/utils": "*",
    "@monorepo/ui": "*"
  }
}
```

npm workspaces automatically symlinks local packages!

---

## Working with Workspaces

### Install Dependencies

```bash
# Install for specific workspace
npm install lodash -w @monorepo/utils

# Install for all workspaces
npm install typescript -ws

# Install devDependency at root
npm install -D prettier
```

### Run Scripts

```bash
# Run script in specific workspace
npm run build -w @monorepo/utils

# Run script in all workspaces
npm run test -ws
```

### Add New Workspace

1. Create folder in `packages/` or `apps/`
2. Add `package.json` with unique name
3. Run `npm install` to link it

---

## Best Practices

### 1. Naming Convention

Use scoped packages: `@monorepo/package-name`

### 2. Dependency Versions

Keep external dependencies aligned across workspaces

### 3. Build Order

Always build shared packages before apps that depend on them

### 4. TypeScript Paths

Use TypeScript project references for better IDE support:

```json
{
  "compilerOptions": {
    "paths": {
      "@monorepo/*": ["packages/*/src"]
    }
  }
}
```

### 5. Independent Versioning

Use tools like `changeset` or `lerna-lite` for publishing packages independently

---

## Common Tasks

### Adding a New Shared Package

```bash
mkdir packages/config
cd packages/config
npm init -y
# Edit package.json to set name: "@monorepo/config"
npm install # Link it to the workspace
```

### Debugging Import Issues

```bash
# Clear all node_modules and reinstall
rm -rf node_modules packages/*/node_modules apps/*/node_modules
npm install
```

### Running Multiple Dev Servers

Use a tool like `concurrently`:

```bash
npm install -D concurrently
```

Add to root `package.json`:

```json
{
  "scripts": {
    "dev": "concurrently \"npm:dev:*\""
  }
}
```

---

## Next Steps

- **Add Turborepo** for faster builds with caching
- **Set up TypeScript** project references
- **Configure ESLint** and Prettier at root
- **Add CI/CD** to build and test on every commit
- **Implement changesets** for versioning and publishing

---

## Resources

- [npm Workspaces Docs](https://docs.npmjs.com/cli/v10/using-npm/workspaces)
- [Turborepo Guide](https://turbo.build/repo/docs)
- [Nx Monorepo Guide](https://nx.dev)
- [Monorepo Tools Comparison](https://monorepo.tools)
