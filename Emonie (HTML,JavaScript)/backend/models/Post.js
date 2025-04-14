    // backend/routes/postRoutes.js
const express = require('express');
const Post = require('../models/Post');
const router = express.Router();
const { authMiddleware } = require('../middleware/auth'); 
// ^ Example: if you have an auth middleware to check JWT tokens

// GET /api/posts - Get all posts (public or only for logged-in users)
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
      authorId: req.user.userId // from JWT
    });
    await newPost.save();
    res.status(201).json({ msg: 'Post created', post: newPost });
  } catch (err) {
    res.status(500).json({ msg: 'Server error', err });
  }
});

// GET /api/posts/:id - Get a single post by ID
router.get('/:id', async (req, res) => {
  try {
    const post = await Post.findById(req.params.id).populate('authorId', 'name');
    if (!post) return res.status(404).json({ msg: 'Post not found' });
    res.json(post);
  } catch (err) {
    res.status(500).json({ msg: 'Server error', err });
  }
});

// PUT /api/posts/:id - Edit a post (requires login, check ownership)
router.put('/:id', authMiddleware, async (req, res) => {
  try {
    const { title, content, image } = req.body;
    const post = await Post.findById(req.params.id);
    if (!post) return res.status(404).json({ msg: 'Post not found' });
    if (post.authorId.toString() !== req.user.userId) {
      return res.status(403).json({ msg: 'Not authorized to edit this post' });
    }
    post.title = title;
    post.content = content;
    post.image = image;
    await post.save();
    res.json({ msg: 'Post updated', post });
  } catch (err) {
    res.status(500).json({ msg: 'Server error', err });
  }
});

// DELETE /api/posts/:id - Delete a post
router.delete('/:id', authMiddleware, async (req, res) => {
  try {
    const post = await Post.findById(req.params.id);
    if (!post) return res.status(404).json({ msg: 'Post not found' });
    if (post.authorId.toString() !== req.user.userId) {
      return res.status(403).json({ msg: 'Not authorized to delete this post' });
    }
    await post.remove();
    res.json({ msg: 'Post deleted' });
  } catch (err) {
    res.status(500).json({ msg: 'Server error', err });
  }
});

module.exports = router;
