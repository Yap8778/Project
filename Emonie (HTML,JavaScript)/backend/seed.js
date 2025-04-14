// backend/seed.js
require('dotenv').config();
const mongoose = require('mongoose');
const Post = require('./models/Post'); // or wherever your Post model is
const User = require('./models/User');

(async function seed() {
  try {
    await mongoose.connect(process.env.MONGO_URI);
    console.log('Connected to MongoDB for seeding');

    // Find a user to assign as author, or create one
    let user = await User.findOne({ email: 'seeduser@example.com' });
    if (!user) {
      user = new User({
        name: 'Seed User',
        email: 'seeduser@example.com',
        password: 'hashedpass' // You can store a hashed password
      });
      await user.save();
    }

    // Insert some posts
    await Post.deleteMany({});
    await Post.insertMany([
      {
        title: 'Welcome to Our Mental Wellness Platform',
        content: 'Here is some sample content for the first post.',
        authorId: user._id
      },
      {
        title: 'Another Interesting Post',
        content: 'We discuss mental health tips and more.',
        authorId: user._id
      }
    ]);

    console.log('Seed data inserted');
    process.exit(0);
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
})();
