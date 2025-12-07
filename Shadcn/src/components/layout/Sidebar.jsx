import { Home, Package, Users, Truck } from "lucide-react"

const Sidebar = () => {
  return (
    <div className="w-64 h-screen bg-[#181818] text-white p-5 flex flex-col gap-6">
      <h2 className="text-xl font-bold">Inventory System</h2>

      <nav className="flex flex-col gap-3">
        <a className="flex items-center gap-2 hover:bg-gray-800 p-2 rounded"><Home size={18}/> Dashboard</a>
        <a className="flex items-center gap-2 hover:bg-gray-800 p-2 rounded"><Package size={18}/> Inventory</a>
        <a className="flex items-center gap-2 hover:bg-gray-800 p-2 rounded"><Truck size={18}/> Suppliers</a>
        <a className="flex items-center gap-2 hover:bg-gray-800 p-2 rounded"><Users size={18}/> Accounts</a>
      </nav>
    </div>
  )
}

export default Sidebar