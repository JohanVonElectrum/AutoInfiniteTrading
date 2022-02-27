const mineflayer = require("mineflayer");
const readline = require("readline");
const express = require("express");
const bodyParser = require("body-parser");

const client = mineflayer.createBot({
    host: process.argv[2],
    port: process.argv[3],
    version: process.argv[4],
    username: process.argv[5],
    password: process.argv[6],
    auth: process.argv[7]
});

client.on("chat", (username, message) => {
    if (username == client.username) return
    console.log(`>${message}`);
});

client.on("login", () => {
    console.log("<login");
});

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.post("/message", (req, res) => {
    client.chat(req.body.message);
    res.sendStatus(200);
});

app.post("/connect", (req, res) => {
    client.connect({
        host: req.body.host,
        port: req.body.port,
        version: req.body.version
    });
    res.sendStatus(200);
});

app.listen(404, () => {
    console.log("AutoInfiniteTrading listening on port 404...");
});