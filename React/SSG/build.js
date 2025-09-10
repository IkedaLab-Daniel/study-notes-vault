import { renderToStaticMarkup } from "react-dom/server"
import { createElement as h } from "react"
import {
    readFileSync,
    writeFileSync,
    existsSync,
    mkdirSync,
    readdirSync,
    unlinkSync
} from 'node:fs';
import { fileURLToPath } from "node:url";
import path, { dirname } from "node:path"
import App from "./app.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const distPath = path.join(__dirname, "dist");

const shell = readFileSync(path.join(__dirname, "index.html"), "utf8");

const app = renderToStaticMarkup(h(App));
const html = shell.replace("<!--ROOT-->", app);

if (!existsSync(path)){
    mkdirSync(distPath)
} else {
    const files = readdirSync(distPath)
    for (const file of files){
        unlinkSync(path.join(distPath, file))
    }
}

writeFileSync(path.join(distPath, "index.html"), html)