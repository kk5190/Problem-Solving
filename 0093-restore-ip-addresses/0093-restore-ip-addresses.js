/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    // Helper function to check if a segment is valid
    function isValid(segment) {
        if (segment.length > 1 && segment[0] === "0") {
            return false;
        }
        return Number(segment) <= 255;
    }
    
    // Helper function to perform backtracking
    function backtrack(s, index, segments, result) {
        // If we have 4 segments, check if we have reached the end of the input string
        if (segments.length === 4) {
            if (index == s.length) {
                result.push(segments.join("."));
            }
            return;
        }

        // Iterate through the remaining characters of the input string
        for (let i=1; i <=3; i++) {
            if (index + 1 > s.length) {
                break;
            }
            let segment = s.substring(index, index + i);
            if (isValid(segment)) {
                backtrack(s, index+i, segments.concat([segment]), result);
            }
        }
    }

    // Initialize an empty array to store the valid IP addresses
    let ans = [];
    // Start the backtracking process
    backtrack(s, 0, [], ans);
    return ans;


    
};