import { Router } from 'express'
import { body, validationResult } from 'express-validator'

const router = Router()

// > products

router.get('/product', (req, res) => {
    res.send('oki')
})
router.get('/product/:id', () => {})
router.put('/product/:id', body('name').isString(), (req, res) => {
    const errors = validationResult(req)

    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() })
    }

    res.send('ok')
})
router.post('/product', () => {})
router.delete('/product/:id', () => {})

// > update

router.get('/update', () => {})
router.get('/update/:id', () => {})
router.put('/update/:id', () => {})
router.post('/update', () => {})
router.delete('/update/:id', () => {})

// > updatepoint

router.get('/updatepoint', () => {})
router.get('/updatepoint/:id', () => {})
router.put('/updatepoint/:id', () => {})
router.post('/updatepoint', () => {})
router.delete('/updatepoint/:id', () => {})

export default router