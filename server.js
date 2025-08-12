const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Backend is live! 🚀');
});

app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello from your free Railway backend!' });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
