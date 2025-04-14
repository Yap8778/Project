const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');

// Register endpoint
router.post('/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;

    // Validate input
    if (!username || !email || !password) {
      return res.status(400).json({
        error: {
          message: 'All fields are required'
        }
      });
    }

    // Check if user already exists
    const existingUser = await User.findOne({
      $or: [{ email }, { username }]
    });

    if (existingUser) {
      return res.status(400).json({
        error: {
          message: existingUser.email === email 
            ? 'Email already registered' 
            : 'Username already taken'
        }
      });
    }

    // Create new user
    const user = new User({
      username,
      email,
      password // Password will be hashed by the pre-save hook
    });

    // Save user to database
    await user.save();

    // Return success response
    res.status(201).json({
      message: 'Registration successful',
      user: {
        id: user._id,
        username: user.username,
        email: user.email
      }
    });
  } catch (error) {
    console.error('Registration error:', error);
    res.status(500).json({
      error: {
        message: 'Server error during registration'
      }
    });
  }
});

module.exports = router;