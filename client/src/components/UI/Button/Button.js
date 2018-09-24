import React from 'react';
import PropTypes from 'prop-types';
import './Button.css';

const button = ({
  children,
  active,
  onClick,
}) => (
  <button
    className={'Button'.concat(`${active ? ' Active' : ''}`)}
    onClick={onClick}
    type="button"
  >
    { children }
  </button>
);

button.propTypes = {
  children: PropTypes.string.isRequired,
  active: PropTypes.bool,
  onClick: PropTypes.func,
};

button.defaultProps = {
  active: false,
  onClick: () => {},
};

export default button;
