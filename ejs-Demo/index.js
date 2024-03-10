import express from "express";

const app = express();
const port = 3000;

const today = new Date();
const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
var advice = "";
var dayType = "";
var dayNumber = today.getDay();



if(dayNumber === 0 || dayNumber === 6){
    dayType = "weekend";
    advice = "have fun!";
}
else{
    dayType = "weekday";
    advice = "work hard!"
}


app.get("/", (req, res) => {
    res.render("index.ejs",
    { 
        day: dayType,
        adv: advice}
    );
});

app.listen(port, () => {
    console.log("listening at port 3000");
});

