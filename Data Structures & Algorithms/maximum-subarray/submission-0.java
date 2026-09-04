class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int maxendingati = nums[0];

        for(int i = 1; i < nums.length; i++) {
            maxendingati = nums[i] > nums[i] + maxendingati? nums[i] : nums[i] + maxendingati;
            max = max > maxendingati? max : maxendingati;
        }

        return max;
    }
}
