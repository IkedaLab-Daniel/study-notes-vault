import jwt from 'jsonwebtoken'
import { Request, Response, NextFunction } from 'express';
import bcrypt from 'bcrypt'
import { error } from 'console';
type User = {
    id: string | number;
    username: string;
};

export const comparePasswords = (password, hash) => {
    return bcrypt.compare(password, hash)
}

export const hashPassword = (password) => {
    const salt = 5
    return bcrypt.hash(password, 5)
}

export const createJWT = (user: User) => {
    const secret = process.env.JWT_SECRET;
    
    if (!secret) {
        throw new Error('JWT_SECRET environment variable is not defined');
    }

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
        console.log("Error: no auth header")
        res.status(401);
        res.json({ "message": "no authorization header"})
        return
    }

    const [, token] = bearer.split(' ');

    if (!token){
        console.log("Error: No token on header")
        res.status(401);
        res.json({ "message": "why no token! ??????"})
        return
    }

    console.log("Someone with auth tried to request")
    next()
}
