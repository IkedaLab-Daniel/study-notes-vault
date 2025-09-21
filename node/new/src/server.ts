import express from 'express'
import router from './router'
const app = express();

app.use('/api', router)

export default app