/* eslint-disable import/extensions */
import express from 'express.js';
import routes from './routes/index.js';

const app = express();
for (const [route, callback] of Object.entries(routes)) {
  app.get(route, callback);
}
app.listen(1245);

export default app;
