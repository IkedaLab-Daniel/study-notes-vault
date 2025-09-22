import prisma from "../src/db";
import { createJWT, hashPassword } from "../src/modules/auth";

export const createNewUser = async (req, res) => {
    const user = await prisma.user.create({
        data: {
            username: req.body.username,
            password: await hashPassword(req.body.password),
        }
    })

    const token = createJWT(user)
    res.json({token})
}