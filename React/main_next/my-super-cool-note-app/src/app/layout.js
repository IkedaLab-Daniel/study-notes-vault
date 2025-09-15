import Link from "next/link";
import "doodle.css/doodle.css";
import "./globals.css";

export const metadata = {
  title: "My Super Cool Note App",
  description: "A simple note-taking app built with Next.js",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="doodle">
        <h1>
          <Link href="/">My Super Cool Note App</Link>
        </h1>
        {children}
        <div style={{margin: '20px', padding: '20px', border: '2px dashed #333'}}>
          Test content with manual styling
        </div>
      </body>
    </html>
  )
}