'use strict';

require('dotenv').config(); // Load variables from .env into process.env

// Retrieve a required environment variable.
// Throw an error if the variable does not exist.
function mustGet(name) {
  const value = process.env[name];

  if (!value) {
    const err = new Error('Missing environment variable: ' + name);
    err.id = 1; // Custom error id
    throw err;
  }

  return value;
}

module.exports = { mustGet }; // Export for other files
