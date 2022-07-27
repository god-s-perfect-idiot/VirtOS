const express = require('express')
const app = express()
const port = 7777

app.get('/ping', (req, res) => {
    res.send('Server Active!')
})

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`)
})