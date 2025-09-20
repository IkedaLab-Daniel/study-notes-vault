const http = require('http')

const server = http.createServer(async (req, res) => {
    if (req.method === 'GET' && req.url === '/'){
        console.log("Hello, server!")
        res.end()
    }   
})

server.listen(3001, () => {
    console.log('Server on http://localhost:3001')
})