/**
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var index = [];
    for (var i = 0; i < nums.length-1; i++) { 
        for (var j =0; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                index = [i, j];
            }
        }
    }
    return index;
};
