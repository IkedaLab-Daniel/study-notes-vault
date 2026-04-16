import Image from "next/image";

export default function Home() {
  return (
    <main>
      <h1 className="text-4xl font-bold mb-2">Hello World</h1>
      <Image 
        src="https://media.tenor.com/v7lgy2BsGR8AAAAe/shocked-black-guy-shocked.png"
        alt="wow"
        width={200}
        height={200}
        priority
      />
    </main>
  );
}
