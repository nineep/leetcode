import itertools
class Solution:
    """
    使用pop(), 删除len(nums)-element_num 个元素，返回此时列表
    0个元素，删除所有，返回[]
    1个元素，删除len(nums)-1个元素，返回列表
    ...
    """
    def subsets(self, nums: list) -> list:
        res = []
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res

    # 迭代
    def subsets2(self, nums):
        res = [[]]
        for i in nums:
            print('before res', res)
            res = res + [[i] + num for num in res]
            print('after res', res)
        return res

    # 递归（回溯算法）
    def subsets3(self, nums):
        res = []
        n = len(nums)
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])
        helper(0, [])
        return res



a = Solution().subsets2([1,2,3])
print(a)




