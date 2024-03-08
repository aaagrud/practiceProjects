import express from "express";
import { dirname } from "path";
import bodyParser from "body-parser";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({
  extended: true
}));

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html")
});

app.post("/submit", (req, res) => {
  var street = req.body["street"];
  var pet = req.body["pet"];
  res.send("band name is: " + street + pet);
});


/*
goal:
1. serve the html page in home
2. get data from it
3. print that data in submit
*/
