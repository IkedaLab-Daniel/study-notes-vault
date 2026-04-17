import Link from "next/link";
import Layout from "../Navigation";

export default function About() {
    return (
        <Layout>
            <h1 className="text-6xl font-bold">About Me</h1>
            <Link href="/">Back</Link>
        </Layout>
    )
}