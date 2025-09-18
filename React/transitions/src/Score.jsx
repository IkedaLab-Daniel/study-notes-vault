const loadingUrl = "../images/loading.webp"

export default function Score({
    isPending,
    home,
    away,
    awayName,
    homeName,
    awayImage,
    homeImage
}) {
    return(
        <div className="score">
            <div>
                <h2>{isPending ? "HOME" : homeName}</h2>
                <h2>{isPending ? "-" : home}</h2>
                <img src={isPending ? loadingUrl : homeImage} alt="home team" />
            </div>
            <div>
                <h2>{isPending ? "AWAY" : awayName}</h2>
                <h2>{isPending ? "-" : away}</h2>
                <img src={isPending ? loadingUrl : awayImage} alt="away team" />
            </div>
        </div>
    )
}