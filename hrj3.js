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


/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function

    // if one element
    let firstLargest = nums[0];
    let secondLargest = nums[0];
    let i = 0;
    //console.log('values %d %d %d %d', i, nums[i], secondLargest, firstLargest);
    if (nums.length > 1) {
        for (i=1; i < nums.length; i++){
            if (nums[i] > firstLargest) {
                //console.log('changing f+s ');
                secondLargest = firstLargest;
                firstLargest = nums[i];
            } else if ((nums[i] > secondLargest) && (nums[i] != firstLargest)){
                //console.log('changing s only');
                secondLargest = nums[i];
            } //else {
                //console.log('changing neither');
            //}
            //console.log('values %d %d %d %d', i, nums[i], secondLargest, firstLargest);
        }
    }
    return secondLargest;
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}