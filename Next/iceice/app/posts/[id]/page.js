import Image from "next/image";
import { posts } from "../../data/posts";
import styles from "./Post.module.css";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";

export default async function Post({ params }) {
    const { id } = await params
    const post = posts.find((post) => post.id === id);

    if (!post) {
        return (
            <h1>! Post not found !</h1>
        )
    }

    return (
        <main className={styles.container}>
            <h1 className={styles.title}>{post.title}</h1>
            <h1 className={styles.content}>{post.content}</h1>
            <Image 
                    src="https://media.tenor.com/v7lgy2BsGR8AAAAe/shocked-black-guy-shocked.png"
                    alt="wow"
                    width={200}
                    height={200}
                    priority
                    className="mb-4"
                  />
            <Link href="/" className="text-sm text-slate-300 flex items-center gap-1 hover:scale-110 hover:text-white hover:font-bold transition duration-500">
                <ArrowLeft size={16} />
                <span>Back</span>
            </Link>
        </main>
    );
}