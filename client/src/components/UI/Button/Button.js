import React from 'react';
import PropTypes from 'prop-types';
import './Button.css';

const button = ({
  children,
  active,
  onClick,
  value,
}) => (
  <button
    className={'Button'.concat(`${active ? ' Active' : ''}`)}
    onClick={onClick}
    type="button"
    value={value}
  >
    { children }
  </button>
);

button.propTypes = {
  children: PropTypes.string.isRequired,
  active: PropTypes.node,
  onClick: PropTypes.func,
  value: PropTypes.node,
};

button.defaultProps = {
  value: false,
  active: false,
  onClick: () => {},
};

export default button;
