import Sidebar from "./Sidebar";

export default function Layout({ children }) {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6 bg-gray-100 min-h-screen">
        {children}
      </div>
    </div>
  );
}