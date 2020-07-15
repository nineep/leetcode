class Solution:
    def merge(self, nums1, m, nums2, n):

        # for i in range(m):
        #     nums1.pop()
        #
        # nums1.extend(nums2)
        # print(nums1)
        # nums1.sort()
        # return nums1

        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1

a = Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(a)
