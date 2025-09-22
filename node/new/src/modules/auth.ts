import jwt from 'jsonwebtoken'
import { Request, Response, NextFunction } from 'express';

type User = {
    id: string | number;
    username: string;
};

export const createJWT = (user: User) => {
    const secret = process.env.JWT_SECRET;
    
    if (!secret) {
        throw new Error('JWT_SECRET environment variable is not defined');
    }
    
    // > convert object to a String
    const token = jwt.sign({
            id: user.id, 
            username: user.username
        }, 
        secret
    )
    return token
}

export const protect = (req: Request, res: Response, next: NextFunction) => {
    const bearer = req.headers.authorization;

    if (!bearer){
        res.status(401);
        res.json({ "message": "no authorization header"})
        return
    }

    console.log("Someone with auth tried to request")
    next()
}
