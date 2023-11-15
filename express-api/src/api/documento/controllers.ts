import { Request, Response } from 'express';

import { docRepo } from '../../data/functions/documentos';
import { validateIn } from '../functions';

async function getDocs(req: Request, res: Response) {
  const docs = await docRepo.find();
  res.status(200).json({
    message: 'Lista de documentos',
    docs,
  });
}

async function addDocs(req: Request, res: Response) {
  if (validateIn(req.body, ['massive'])) {
    const docsReq = req.body.massive;
    const docs = docRepo.create(docsReq);
    const savedDoc = await docRepo.save(docs);
    res.status(201).json({
      message: 'Documentos creados con éxito',
      doc: savedDoc,
    });
    return;
  }
  if (!validateIn(req.body, ['titulo', 'contenido'])) {
    res.status(400).json({
      message: 'Error: No se han recibido todos los datos necesarios',
    });
    return;
  }
  const { titulo, contenido } = req.body;
  const doc = docRepo.create({ titulo, contenido });
  const savedDoc = await docRepo.save(doc);
  res.status(201).json({
    message: 'Documento creado con éxito',
    doc: savedDoc,
  });
}

export default { getDocs, addDocs };
