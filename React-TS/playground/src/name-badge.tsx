const NameBadge = ({ name }: { name: string }) => {
    return (
        <section className="badge">
            <header className="badge-header">
                <h1 className="text-5xl">Hello</h1>
                <p>My name is...</p>
            </header>
            <div className="badge-body">
                <p className="badge-name">{name}</p>
            </div>
            <footer className="badge-footer" />
        </section>
    );
};

export default NameBadge;