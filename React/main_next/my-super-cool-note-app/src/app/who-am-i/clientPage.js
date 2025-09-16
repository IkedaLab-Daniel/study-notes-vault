import updateUsername from './updateUsername';

export default function ClientWhoAmI({ children, id }) {
    return(
        <div>
            {children}
            <form action={updateUsername}>
                <h2>Enter new username</h2>
                <input type='text' name='username' placeholder='username' />
                <input type="hidden" name="id" value={id} />
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}