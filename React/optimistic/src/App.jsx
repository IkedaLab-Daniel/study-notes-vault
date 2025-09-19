import { useEffect, useState } from "react";

export default function App() {
  const [thoughts, setThoughts] = useState([]);
  const [thought, setThought] = useState("");

  async function postDeepThought() {
    setThought("");
    const response = await fetch("/thoughts", {
      method: "POST",
      headers: {
        "Content-Type" : "application/json"
      },
      body: JSON.stringify({ thought }),
    });
    
    if (!response.ok) {
      alert("This thought was not deep enough. Do bettter.")
      return;
    }

    const { thoughts: newThoughts } = await response.json();
    setThought(newThoughts);
  }

  useEffect(() => {
    fetch("/thoughts")
      .then((res) => res.json)
      .then((data) => {
        setThoughts(data);
      });
  }, [])
}