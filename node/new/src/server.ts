import express from 'express'
import router from './router'
const app = express();

app.get("/", (req, res) => {
    console.log("Hello from express")
    res.status(200)
    res.json({ message: "hellor" })
})

app.use('/api', router)

export default app