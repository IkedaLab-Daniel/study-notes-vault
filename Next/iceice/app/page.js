import Image from "next/image";
import Link from "next/link";
import Layout from "./Navigation";

export default function Home() {
  return (
    <Layout>
      <h1 className="text-4xl font-bold mb-2">Welcome to our Homepage</h1>
      <Image 
        src="https://media.tenor.com/v7lgy2BsGR8AAAAe/shocked-black-guy-shocked.png"
        alt="wow"
        width={200}
        height={200}
        priority
      />
      <div className="flex flex-col items-center gap-2">
        <Link href="/about" className="hover:font-bold hover:text-blue-600 transition duration-700">Go to About Page</Link>
        <Link href="/posts/1" className="hover:font-bold hover:text-blue-600 transition duration-700">Go to Post 1</Link>
        <Link href="/posts/2" className="hover:font-bold hover:text-blue-600 transition duration-700">Go to Post 2</Link>
        <p>Your API Key is: {process.env.NEXT_PUBLIC_API_KEY}</p>
      </div>
      
    </Layout>
  );
}
