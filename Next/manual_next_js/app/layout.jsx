export default function RootLayout({ children }) {
  return (
    <html lang="en" style={{background: 'black', color: 'white'}}>
      <body>{children}</body>
    </html>
  )
}