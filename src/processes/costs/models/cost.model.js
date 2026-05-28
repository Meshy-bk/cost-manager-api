'use strict';

const mongoose = require('mongoose');

// Define MongoDB schema for cost items
const CostSchema = new mongoose.Schema(
  {
    description: { type: String, required: true, trim: true }, // Cost description
    category: {
      type: String,
      required: true,
      enum: ['food', 'health', 'housing', 'sports', 'education'] // Allowed categories
    },
    userid: { type: Number, required: true }, // User id who owns this cost
    sum: { type: mongoose.Schema.Types.Double, required: true, min: 0 } // Cost amount, stored as a BSON Double (must be >= 0)
  },
  {
    collection: 'costs', // MongoDB collection name
    versionKey: false,
    timestamps: true // Auto add createdAt / updatedAt
  }
);

module.exports = mongoose.model('Cost', CostSchema); // Export Cost model
