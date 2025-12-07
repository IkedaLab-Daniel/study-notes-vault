import { Card, CardContent } from "@/components/ui/card";

export default function Dashboard() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">
        Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card>
          <CardContent>
            <h2 className="text-sm text-gray-500">Total Items</h2>
            <p className="text-2xl font-bold">1,200</p>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-5">
            <h2 className="text-sm text-gray-500">Low Stock</h2>
            <p className="text-2xl font-bold">32</p>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-5">
            <h2 className="text-sm text-gray-500">Suppliers</h2>
            <p className="text-2xl font-bold">18</p>
          </CardContent>
        </Card>

      </div>
    </div>
  )
}