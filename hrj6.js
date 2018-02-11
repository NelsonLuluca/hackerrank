'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}


/*
*   Return the largest value of any a & b < k in S (where a < b).
*   
*   n: Set S is a sequence of distinct integers from 1 to n (i.e., {1, 2, ..., n}).
*   k: An integer.
*/
function getMaxLessThanK(n, k) {
    
    let theMax = 0;
    let i = 0; let j = 0;
    for (i = 1; i <= n; i++) {

        for (j = i+1; j <= n; j++){
            //console.log('n=%d k=%d i=%d j=%d', n, k, i, j)
            let bitand = i & j;
            if ((bitand > theMax) && (bitand < k)){
                theMax = bitand;
            }
        }
    }
    return theMax;
}


function main() {
    const q = +(readLine());
    
    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(' ').map(Number);
        
        console.log(getMaxLessThanK(n, k));
    }
}
