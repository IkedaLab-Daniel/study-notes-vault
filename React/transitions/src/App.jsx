import { useState, useEffect, useTransition } from "react";
import Score from "./Score";
import getScore from "./getScore";

export default function App() {
  const [isPending, startTransition] = useTransition();
  const [game, setGame] = useState(1);
  const [score, setScore] = useState({ home: "–", away: "–" });

  async function getNewScore(game) {
    setGame(game);

    startTransition(async () => {
      const newScore = await getScore(game);
  
      startTransition(() => {
        setScore(newScore);
      });
    });
  }

  useEffect(() => {
    getNewScore(game);
  }, []);

  return (
    <div className="app">
      <h1>Game {game}</h1>
      <select
        onChange={(e) => {
          getNewScore(e.target.value);
        }}
      >
        <option value={1}>Game 1</option>
        <option value={2}>Game 2</option>
        <option value={3}>Game 3</option>
        <option value={4}>Game 4</option>
        <option value={5}>Game 5</option>
        <option value={6}>Game 6</option>
        <option value={7}>Game 7</option>
      </select>
      <div className={`loading-container ${isPending ? "loading" : ""}`}>
        {" "}
        <span className="spinner">⚽️</span>
      </div>
      <div>
        <Score
          isPending={isPending}
          homeImage={score.homeImage}
          homeName={score.homeName}
          awayImage={score.awayImage}
          awayName={score.awayName}
          home={score.home}
          away={score.away}
        />
      </div>
    </div>
  );
}