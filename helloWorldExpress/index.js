import express from "express";
const port = 3000;
const app = express();

app.listen(port, () =>{
    console.log("hello from express and node!")
})

app.get("/", (req, res) => {
    res.send("<p>Hello World!</p>")
});

app.get("/about", (req, res) => {
    res.send("<p>I am Durga!</p>")
});

app.get("/contact", (req, res) => {
    res.send("<p>Number: 6238881692</p>")
});
