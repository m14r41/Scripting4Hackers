const express = require("express");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = 3000;

/* absolute static path */
app.use(express.static(path.join(__dirname, "public")));

/*  ROOT ROUTE */
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "index.html"));
});

/* Read helper */
function read(file) {
    try {
        return fs.readFileSync(file, "utf8")
            .split("\n")
            .filter(Boolean);
    } catch {
        return [];
    }
}

/* API: list targets */
app.get("/api/targets", (req, res) => {
    const dirs = fs.readdirSync(__dirname)
        .filter(f =>
            fs.existsSync(path.join(__dirname, f)) &&
            fs.lstatSync(path.join(__dirname, f)).isDirectory()
        );

    res.json(dirs);
});

/* API: target data */
app.get("/api/data/:target", (req, res) => {

    const t = req.params.target;
    const base = path.join(__dirname, t);

    res.json({
        target: t,
        subs: read(path.join(base, "all_subs.txt")),
        live: read(path.join(base, "alive.txt")),
        vuln: read(path.join(base, "nuclei.txt"))
    });
});

app.listen(PORT, () => {
    console.log(`Running: http://localhost:${PORT}`);
});