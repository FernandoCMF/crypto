const fs = require('fs');
const crypto = require('node:crypto');

const alg = 'aes-256-ctr';
const passwd = 'abcdacbd';

const read = fs.createReadStream('teste.txt');
const write = fs.createWriteStream('testeOutput.txt');
const cipher = crypto.createCipher(alg, passwd);

read.pipe(cipher).pipe(write);
