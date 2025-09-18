import http from "node:http";
import deepThoughts from "./deepThoughts.js";

const DELAY = 5000; // 5 seconds
const ERROR_RATE = 0.2; // 20% of requests will fail

let thoughts = [...deepThoughts];

const server = http.createServer(async (req, res) => {
  if (req.method === "GET" && req.url === "/thoughts") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(thoughts));
  } else if (req.method === "POST" && req.url === "/thoughts") {
    await new Promise((resolve) => setTimeout(resolve, DELAY));
    let body = "";
    req.on("data", (chunk) => {
      body += chunk.toString();
    });
    req.on("end", () => {
      if (Math.random() < ERROR_RATE) {
        res.writeHead(400, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: "Your thought was not deep enough." }));
        return;
      }

      const { thought: newThought } = JSON.parse(body);
      thoughts = [newThought, ...thoughts];
      res.writeHead(201, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ thoughts }));
    });
  } else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Not Found");
  }
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});
