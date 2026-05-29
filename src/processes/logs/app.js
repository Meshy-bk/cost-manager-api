'use strict';

const express = require('express');
const logger = require('../../config/logger');
const errorHandler = require('../../shared/middleware/error-handler.middleware');
const { buildRouter } = require('./routes');
const requestLogMiddleware = require('../../shared/middleware/request-logger.middleware');

function buildApp() {
  const app = express();

  app.use(express.json()); // Parse JSON requests
  app.use(requestLogMiddleware('logs')); // Log requests for the logs service

  app.get('/health', function (req, res) {
    logger.info({ endpoint: '/health' }, 'logs health check'); // Health check log
    res.json({ ok: true });
  });

  app.use('/api', buildRouter()); // Main API routes

  app.use(errorHandler); // Global error handler

  return app;
}

module.exports = { buildApp }; // Export app builder
