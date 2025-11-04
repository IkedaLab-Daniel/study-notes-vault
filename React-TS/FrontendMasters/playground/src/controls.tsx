import PropTypes from 'prop-types';

type ControlPannelProps = {
    name: string;
    onChange: any;
}

const ControlPanel = ({ name, onChange } : ControlPannelProps) => {
  return (
    <form
      className="flex flex-row gap-4 text-white bg-primary-10"
      onSubmit={(event) => event.preventDefault()}
    >
      <div>
        <label className="font-bold">Your Name</label>
        <input
          name="name"
          className="w-full"
          type="text"
          value={name}
          onChange={onChange}
        />
      </div>
    </form>
  );
};

ControlPanel.propTypes = {
  name: PropTypes.string,
  onChange: PropTypes.func,
};

export default ControlPanel;