class Solution:
    """
    输入: [1,2,3]
    输出:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
    """
    # 列表一位元素和其它元素互换位置
    def exchange(self, ls, m, n):
        ls[m], ls[n] = ls[n], ls[m]

    def l_offset(self, ls, n):
        for i in range(n):
            ls.insert(0, ls.pop())
        return ls

    def permute(self, nums: list):

        # new_list = []
        # for i in range(len(nums)):
        #     print('==========================')
        #     print('初始new list', new_list)
        #     # ls_template = nums
        #     # print('ls_template', ls_template)
        #     for ii in range(len(nums)):
        #         print('--------')
        #         ls_template = nums.copy()
        #         print('初始定义ls_template（=nums）', ls_template)
        #
        #         # print(i,ii)
        #         if i != ii:
        #             # print(i,ii,'交换')
        #             self.exchange(ls_template, i, ii)
        #             print('交换:', i, ii, '元素位置后ls_template', ls_template)
        #             print('添加模板列表前的new list', new_list)
        #             if ls_template not in new_list:
        #                 new_list.append(ls_template)
        #             print('添加模板列表后的new list', new_list)

        # new_list = []
        # for i in range(len(nums)):
        #
        #     print('--------')
        #     print('初始new list', new_list)
        #     print('初始nums', nums)
        #
        #     offset_ls = self.l_offset(nums, 1)
        #     print('位移后offset_ls', offset_ls, id(offset_ls))
        #
        #     new_list.append(offset_ls)
        #     print('位移后new_list', new_list, id(new_list))
        #
        # return new_list

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


a = Solution().permute([1, 2, 3])
print(a)
