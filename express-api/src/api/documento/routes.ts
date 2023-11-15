import express from 'express';

import middlewares from '../middlewares';
import docControllers from './controllers';

const docRoutes = express.Router();

docRoutes.get('/documento', docControllers.getDocs);
docRoutes.post('/documento', middlewares.authGuard, docControllers.addDocs);

export default docRoutes;
