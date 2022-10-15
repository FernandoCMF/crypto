const fs = require('fs');
const crypto = require('node:crypto');

const alg = 'aes-256-ctr';
const passwd = 'abcdacbd';

const read = fs.createReadStream('testeOutput.txt');
const write = fs.createWriteStream('decrypted.txt');
const cipher = crypto.createDecipher(alg, passwd);

read.pipe(cipher).pipe(write);
