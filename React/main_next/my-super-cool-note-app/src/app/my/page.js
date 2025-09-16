import { AsyncDatabase } from "promised-sqlite3";

// this page assumes that you are logged in as user 1
export default async function MyNotes() {
  async function fetchNotes() {
    const db = await AsyncDatabase.open("./notes.db");
    const fromPromise = db.all(
      "SELECT n.id as id, n.note as note, f.name as from_user, t.name as to_user FROM notes n JOIN users f ON f.id = n.from_user JOIN users t ON t.id = n.to_user WHERE from_user = ?",
      ["1"]
    );
    const toPromise = db.all(
      "SELECT n.id as id, n.note as note, f.name as from_user, t.name as to_user FROM notes n JOIN users f ON f.id = n.from_user JOIN users t ON t.id = n.to_user WHERE to_user = ?",
      ["1"]
    );
    const [from, to] = await Promise.all([fromPromise, toPromise]);
    return {
      from,
      to,
    };
  }

  const notes = await fetchNotes();

  return (
    <div>
      <h1>My Notes</h1>
      <fieldset>
        <legend>Notes To You</legend>
        <table>
          <thead>
            <tr>
              <th>From</th>
              <th>To</th>
              <th>Note</th>
            </tr>
          </thead>
          <tbody>
            {notes.to.map(({ id, note, from_user, to_user }) => (
              <tr key={id}>
                <td>{from_user}</td>
                <td>{to_user}</td>
                <td>{note}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </fieldset>
      <fieldset>
        <legend>Notes From You</legend>
        <table>
          <thead>
            <tr>
              <th>From</th>
              <th>To</th>
              <th>Note</th>
            </tr>
          </thead>
          <tbody>
            {notes.from.map(({ id, note, from_user, to_user }) => (
              <tr key={id}>
                <td>{from_user}</td>
                <td>{to_user}</td>
                <td>{note}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </fieldset>
    </div>
  );
}