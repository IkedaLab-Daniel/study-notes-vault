# Tailwind CSS Playground

A simple setup for learning and experimenting with Tailwind CSS.

## Quick Start

1. Open `index.html` in your browser
2. Start editing the HTML with Tailwind classes
3. IntelliSense should work automatically in VS Code

## Features

- ✅ Tailwind CSS via CDN (no build process needed)
- ✅ IntelliSense support for VS Code
- ✅ Responsive design examples
- ✅ Custom configuration for extended classes
- ✅ Live server options

## Running a Local Server

### Option 1: Python (if you have Python installed)
```bash
npm run serve
# or directly:
python3 -m http.server 8000
```

### Option 2: PHP (if you have PHP installed)
```bash
npm run serve-alt
# or directly:
php -S localhost:8000
```

### Option 3: VS Code Live Server Extension
1. Install "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

## IntelliSense Setup

Make sure you have the "Tailwind CSS IntelliSense" extension installed in VS Code:
1. Go to Extensions (Cmd+Shift+X)
2. Search for "Tailwind CSS IntelliSense"
3. Install the official extension by Tailwind Labs

## File Structure

```
Tailwind/
├── index.html          # Main playground file
├── tailwind.config.js  # Tailwind configuration
├── package.json        # Project configuration
├── .vscode/
│   └── settings.json   # VS Code settings for IntelliSense
└── README.md          # This file
```

## Example Classes to Try

- Layout: `flex`, `grid`, `container`, `mx-auto`
- Spacing: `p-4`, `m-8`, `space-x-4`, `gap-6`
- Colors: `bg-blue-500`, `text-red-600`, `border-gray-300`
- Typography: `text-xl`, `font-bold`, `leading-relaxed`
- Effects: `shadow-lg`, `rounded-lg`, `hover:scale-105`

Happy coding! 🎨
