import Image from "next/image"

export default async function Post({ params }) {
    const { id } = await params

    return (
        <main className="flex flex-col justify-center items-center gap-2">
            <h1 className="text-4xl">Post ID: {id}</h1>
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