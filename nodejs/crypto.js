const crypto = require('crypto');

let mypassword = '12345678912345678912345678912345';

let iv = Buffer.from(crypto.randomBytes(16));

var mykey = crypto.createCipheriv('aes-128-cbc', Buffer.from(mypassword), iv);
var mystr = mykey.update('abc', 'utf-8', 'hex');

mystr += mykey.final('hex');

console.log(mystr);
