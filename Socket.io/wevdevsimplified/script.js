// Import socket.io from CDN (loaded via script tag in HTML)
const socket = io('http://localhost:3001')

// Connection event listeners
socket.on('connect', () => {
    console.log('Connected to server! Socket ID:', socket.id)
})

socket.on('connect_error', (error) => {
    console.error('Connection error:', error)
})

socket.on('disconnect', () => {
    console.log('Disconnected from server')
})

const joinRoomButton = document.getElementById("room-button")
const messageInput = document.getElementById("message-input")
const roomInput = document.getElementById("room-input")
const form = document.getElementById("form")

form.addEventListener("submit", e => {
    e.preventDefault()
    const message = messageInput.value
    const room = roomInput.value

    if (message == "") return 
    displayMessage(message)

    messageInput.value = ""
})

joinRoomButton.addEventListener("click", () => {
    const room = roomInput.value
})

function displayMessage(message){
    const div = document.createElement("div")
    div.textContent = message
    document.getElementById("message-container").append(div)
}