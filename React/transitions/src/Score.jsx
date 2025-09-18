const loadingUrl = "/images/loading.webp";
export default function Score({
  isPending,
  home,
  away,
  awayName,
  homeName,
  awayImage,
  homeImage,
}) {
  return (
    <div className="score">
      <div>
        <h2>{isPending ? "HOME" : homeName}</h2>
        <h3>{isPending ? "–" : home}</h3>
        <img src={isPending ? loadingUrl : homeImage} alt="home team logo" />
      </div>
      <div>
        <h2>{isPending ? "AWAY" : awayName}</h2>
        <h3>{isPending ? "–" : away}</h3>
        <img src={isPending ? loadingUrl : awayImage} alt="away team logo" />
      </div>
    </div>
  );
}