import ClientPage from "./clientPage";
import WhoAmI from "./whoAmI";

export default async function WhoAmIPage() {
    return (
        <ClientPage id={1}>
            <WhoAmI />
        </ClientPage>
    );
}