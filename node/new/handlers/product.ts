import prisma from "../src/db"

export const getProducts = async (req, res) => {
    const user = await prisma.user.findUnique({
        where: {
            id: req.user.id
        },
        include: {
            Product: true
        }
    })
    
    if (!user || user.Product.length === 0){
        return res.status(200).json({ "message": "No products yet"})
    }

    res.status(200).json({ data: user.Product })
}

export const getUniqueProduct = async (req, res) => {
    const id = req.params.id
    const product = await prisma.product.findUnique({
        where: {
            id,
            belongsTo: req.user.id
        }
    })

    if (!product){
        return res.status(404).json({ "message": "Not found"})
    }

    res.json({ product })
}