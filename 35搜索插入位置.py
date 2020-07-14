class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        for i in range(len(nums)):
            if target < nums[i]:
                print('开始位置')
                return 0
            elif target > nums[-1]:
                print('结束位置')
                return len(nums)
            elif target == nums[i]:
                print('包含')
                return i
            elif nums[i] < target < nums[i+1]:
                print('中间位置')
                return i+1


a = Solution().searchInsert([1,3,5,6],3)
print(a)