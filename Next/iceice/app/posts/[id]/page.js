import Image from "next/image"
import { posts } from "../../data/posts"

export default async function Post({ params }) {
    const { id } = await params
    const post = posts.find((post) => post.id === id);

    if (!post) {
        return (
            <h1>! Post not found !</h1>
        )
    }

    return (
        <main className="flex flex-col justify-center items-center gap-2">
            <h1 className="text-4xl">Post ID: {post.id}</h1>
            <h1 className="text-4xl">Post Title: {post.title}</h1>
            <h1 className="text-4xl">Post Content: {post.content}</h1>
            <Image 
                    src="https://media.tenor.com/v7lgy2BsGR8AAAAe/shocked-black-guy-shocked.png"
                    alt="wow"
                    width={200}
                    height={200}
                    priority
                  />
        </main>
    )
}