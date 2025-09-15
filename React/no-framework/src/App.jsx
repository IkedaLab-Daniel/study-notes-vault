import { Suspense } from "react";
import ServerComponent from "./ServerComponent";
import ClientComponent from "./ClientComponent";

export default function App() {
  console.log("rendering App server component");
  return (
    <Suspense fallback={<h1>Loading...</h1>}>
      <h1>Notes App</h1>
      <ServerComponent />
      <ClientComponent />
    </Suspense>
  );
}