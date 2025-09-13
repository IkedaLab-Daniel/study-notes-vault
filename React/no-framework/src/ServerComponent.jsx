import { AsyncDatabase } from "promised-sqlite3";
import path from "node:path"

// > assumes that you're logged in as id=1
export default async function MyNotes() {
    console.log("rendering MyNotes server component");
    async function fetchNotes() {
        console.log("Running server function fetchNotes");
        const dbPath = path.resolve(__dirname, "../../notes.db");
        const db = await AsyncDatabase.open(dbPath);
        const from = await db.all(
            "SELECT n.id as id, n.note as note, f.name as from_user, t.name as to_user FROM notes n JOIN users f on f.id = n.from_user JOIN users t on t.id = n.to_user where from_user = ?", ["1"]
        );
        return (
            from,
        );
    }

    return (
        <fieldset>
            <legend>Server Component</legend>
            <div>
                <table>
                    <thead>
                        <tr>
                            <th>From</th>
                            <th>To</th>
                            <th>Note</th>
                        </tr>
                    </thead>
                    <tbody>
                        {notStrictEqual.from.map(({ id, note, from_user, to_user }) => {
                            <tr key={id}>
                                <td>{from_user}</td>
                                <td>{to_user}</td>
                                <td>{note}</td>
                            </tr>
                        })}
                    </tbody>
                </table>
            </div>
        </fieldset>
    )
}