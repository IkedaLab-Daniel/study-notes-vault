import prisma from "../src/db"

export const getOneUpdate =  async (req, res) => {
    const update = await prisma.update.findUnique({
        where: {
            id: req.params.id
        }
    })

    res.status(200).json({ update })
}


export const getUpdates = async (req, res) => {
    const products = await prisma.product.findMany({
        where: {
            belongsToId: req.user.id
        },
        include: {
            Update: true
        }
    })

    if (products.length === 0){
        return res.status(200).json({ "message": "No product update yet"})
    }

    const updates = products.reduce((allUpdates, product) => {
        return [...allUpdates, ...product.Update]
    }, [])

    res.status(200).json({ updates })
}

export const updateUpdate = async (req, res) => {
    const products = await prisma.product.findMany({
        where: {
            belongsToId: req.user.id,
        },
        include: {
            Update: true
        }
    })

    const updates = products.reduce((allUpdates, product) => {
        return [...allUpdates, ...product.Update]
    }, [])

    const update = updates.find(update => update.id === req.params.id)

    if (!update) {
        return res.status(404).json({ message: "Update not found" })
    }

    const updatedUpdate = await prisma.update.update({
        where: {
            id: req.params.id
        },
        data: req.body
    })

    res.status(200).json({ update: updatedUpdate })
}