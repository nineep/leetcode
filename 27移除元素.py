class Solution:
    def removeElement(self, nums: list, val: int):
        ls = []
        for i in range(len(nums)):
            if nums[i] == val:
                print('删除第', i, '元素', nums[i])
                ls.append(i)
        new_len = len(nums) - len(ls)
        print(ls)

        count = 0
        for i in ls:
            print(i)
            i -= count
            count += 1
            print(i)
            nums.pop(i)
            print(nums)

        print(nums)
        return new_len


a = Solution().removeElement([3,2,2,3], 3)
print(a)
