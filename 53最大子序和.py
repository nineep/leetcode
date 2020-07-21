class Solution:
    def maxSubArray(self, nums: list) -> int:
        tmp = nums[0]
        max_sum = tmp

        for i in range(1, len(nums)):
            if tmp + nums[i] > nums[i]:
                max_sum = max(max_sum, tmp+nums[i])
                tmp = tmp + nums[i]
            else:
                max_sum = max(max_sum, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]
        return max_sum


a = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(a)