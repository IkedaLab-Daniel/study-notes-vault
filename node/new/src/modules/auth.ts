import jwt from 'jsonwebtoken'
import { Request, Response, NextFunction } from 'express';

type User = {
    id: string | number;
    username: string;
};

// ! Extend Express Request interface to include 'user'
declare global {
    namespace Express {
        interface Request {
            user?: string | object;
        }
    }
}

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

    const [, token] = bearer.split(' ');

    if (!token){
        res.status(401);
        res.json({ "message": "why no token! ??????"})
        return
    }

    try {
        const secret = process.env.JWT_SECRET;
        if (!secret) {
            throw new Error('JWT_SECRET environment variable is not defined');
        }
        const user = jwt.verify(token, secret);
        req.user = user;
        next();
    } catch (err){
        console.error("invalid credentials")
        res.status(401)
        res.json({ "message": "invalid credentials"})
    }


    console.log("Someone with auth tried to request")
    next()
}
