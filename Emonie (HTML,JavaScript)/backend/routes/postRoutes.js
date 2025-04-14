// backend/routes/postRoutes.js
const express = require('express');
const Post = require('../models/Post');
const { authMiddleware } = require('../middleware/auth');

const router = express.Router();

// GET /api/posts - Get all posts (sorted by newest)
router.get('/', async (req, res) => {
  try {
    const posts = await Post.find().sort({ createdAt: -1 }).populate('authorId', 'name');
    res.json(posts);
  } catch (err) {
    res.status(500).json({ msg: 'Server error', err });
  }
});

// POST /api/posts - Create a new post (requires login)
router.post('/', authMiddleware, async (req, res) => {
  try {
    const { title, content, image } = req.body;
    const newPost = new Post({
      title,
      content,
      image,
      authorId: req.user.userId
    });
    await newPost.save();
    res.status(201).json({ msg: 'Post created', post: newPost });
  } catch (err) {
    res.status(500).json({ msg: 'Server error', err });
  }
});

// Additional routes for GET single post, PUT (edit) and DELETE can be added similarly

module.exports = router;
