const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.send('Hello World')
})
app.get('/andrey', function (req, res) {
    res.send('Ola mundo')
})
app.listen(3000,function(){console.log("Servidor funcionando")})