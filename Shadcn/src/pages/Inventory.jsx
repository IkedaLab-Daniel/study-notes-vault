import { TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";

const data = [
  { name: "laptop", qty: 10, supplier: "ABC Cord"},
  { name: "Mouse", qty: 15, supplier: "IceIce LTD"}
];

export default function Inventory() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Inventory</h1>

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Item</TableHead>
            <TableHead>Quantity</TableHead>
            <TableHead>Suppliers</TableHead>
          </TableRow>
        </TableHeader>

        <TableBody>
          {data.map((item, i) => {
            <TableRow key={i}>
                <TableCell>{item.name}</TableCell>
                <TableCell>{item.qty}</TableCell>
                <TableCell>{item.supplier}</TableCell>
            </TableRow>
          })}
        </TableBody>
      </Table>
    </div>
  )
}