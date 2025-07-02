export const SetCounter = ({ onSubmit }) => {
    
  return (
    <section>
      <form
        onSubmit={(event) => {
          event.preventDefault();
          const value = event.target.elements['set-to'].value
          onSubmit(parseInt(value))
        }}
      >
        <label htmlFor="set-to">Set Count</label>
        <input id="set-to" type="number" />
        <input type="submit" />
      </form>
    </section>
  );
};