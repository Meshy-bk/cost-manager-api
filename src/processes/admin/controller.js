'use strict';

const { logEndpointAccess } = require('../../shared/utils/endpoint-logger');

async function getAbout(req, res, next) {
  try {
    await logEndpointAccess(req, 'admin', 'GET /api/about'); // Save this endpoint access to logs

    res.json([
      { first_name: 'Meshy', last_name: 'Bukris' },
      { first_name: 'Shaked', last_name: 'Shlomo' }
    ]);
  } catch (err) {
    next(err); // Send error to the global error handler
  }
}

module.exports = { getAbout }; // Export controller
