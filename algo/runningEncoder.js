const { count } = require("console");

function encode(str) {
    str = str.split('');
    let prevChar = '';
    let counter = 0;
    let opStr = "";
    if (!str)
        return "";
    for (let i = 0; i < str.length; i++) {
        if (prevChar == str[i]) {
            counter++;
        } else {
            if (i != 0) {
                opStr = opStr + counter + prevChar;
            }
            counter = 1;
            prevChar = str[i];
        }
    }
    opStr = opStr + counter + prevChar;
    return opStr;
}

console.log(encode("aaabbccabcccccaa"));