import { Router } from 'express'
import { body } from 'express-validator'
import { handleInputErrors } from './modules/middleware'
import { getProducts } from '../handlers/product'

const router = Router()

// > products

router.get('/product', getProducts)
router.get('/product/:id', () => {})
router.put('/product/:id', body('name').isString(), handleInputErrors, (req, res) => {
    res.send('ok')
})
router.post('/product', body('title', 'body').isString(), handleInputErrors, (req, res) => {
    res.send('ok')
})
router.delete('/product/:id', () => {})

// > update

router.get('/update', () => {})
router.get('/update/:id', () => {})
router.put('/update/:id', () => {})
router.post('/update', body('title', 'body').isString(), () => {})
router.delete('/update/:id', () => {})

// > updatepoint

router.get('/updatepoint', () => {})
router.get('/updatepoint/:id', () => {})
router.put('/updatepoint/:id', () => {})
router.post('/updatepoint',body('title', 'body').isString(), () => {})
router.delete('/updatepoint/:id', () => {})

export default router