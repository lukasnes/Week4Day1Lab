const express = require('express')
const app = express()
const cors = require('cors')

app.use( express.json() )
app.use( cors() )


app.get('/api/users', (req,res) =>{
    let friends = ["Nitin", "Eric", "Jeddy", "Cameron", "Riley"]
    res.status(200).send(friends)
})
app.get("/weather/:temperature", (req, res) => {
    const { temperature } = req.params
    const phrase = `<h3>It was ${temperature} today</h3>`
    res.status(200).send(phrase)
  })


app.listen(4000, console.log('Server running on 4000'))