const io = require('socket.io')(3001, {
    cors: {
        origin: "*", // Allow all origins for development (use specific origins in production)
        methods: ["GET", "POST"]
    }
})

io.on('connection', socket => {
    console.log('New connection:', socket.id)
    
    socket.on('disconnect', () => {
        console.log('User disconnected:', socket.id)
    })
})

console.log("Server On")