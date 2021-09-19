const express = require('express');
const app = express();
const multer = require('multer');
const upload = multer({});
const fs = require('fs').promises;
const { createWriteStream } = require('fs');

const child_process = require('child_process');
const bodyParser = require('body-parser');

const script = 'python ./process.py';

app.use(express.static('./public'))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}));
app.post('/upload', upload.single('img'), async (req, res) => {
	const folder = Math.random().toString(16).slice(2);
	await fs.mkdir(folder);
	
	try {
		let ext = '';
		if (/png/i.test(req.file.mimetype)) ext = '.png';
		else if (/jpe?g/i.test(req.file.mimetype)) ext = '.jpg'
		await fs.writeFile(`${folder}/img${ext}`, req.file.buffer);

		const p = child_process.execSync(`${script} {folder}/img.png ${parseFloat(req.body.x)} ${parseFloat(req.body.y)}`);

		res.send(p.toString());
	}
	catch (e) {
		res.status(404).send("Bad request");
	}
	await fs.rmdir(folder, { recursive: true });
});

app.listen(8080, '0.0.0.0');
