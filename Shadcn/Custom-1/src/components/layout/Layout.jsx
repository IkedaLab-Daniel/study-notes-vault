import Sidebar from "./Sidebar";

export default function Layout({ children }) {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6 bg-[#0a0a0a] min-h-screen text-slate-200">
        {children}
      </div>
    </div>
  );
}