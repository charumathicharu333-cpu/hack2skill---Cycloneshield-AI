import { readFile, writeFile } from "node:fs/promises"

const index = await readFile("frontend/index.html", "utf8")
const css = await readFile("frontend/styles.css", "utf8")
const mapFix = await readFile("frontend/map-fix.css", "utf8")
const source = await readFile("frontend/src/app.js", "utf8")
const js = source.replace(/const API = [^;]+;/, "const API = 'http://localhost:8000';")
const preview = index
  .replace('  <link rel="stylesheet" href="/styles.css">', `<style>${css}</style><style>${mapFix}</style>`)
  .replace('  <link rel="stylesheet" href="/map-fix.css">', "")
  .replace('<script type="module" src="/src/app.js"></script>', `<script>${js}</script>`)

await writeFile("../outputs/CycloneShield-AI-preview.html", preview)
