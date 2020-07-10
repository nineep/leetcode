class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        ( +1, ) -1, 为0则配对成功
        count: 计数（ 或者 ） 出现的次数
        count_repeat:计数 （重复出现的次数
        """
        if len(s) == 1 or s == ")(":
            return 0
        else:
            count = count_repeat = 0
            result = 0

            for i in range(len(s)):
                print('-----------------')
                print('res0', result)

                if s[i] == '(':
                    count += 1
                    count_repeat += 1
                else:
                    count -= 1

                print('count', count)
                if count == 0:
                    print("count_left", count_repeat)
                    print('res1', result)
                    result += (2 * count_repeat)
                    count_repeat = 0
                    print('res2', result)
                # elif count == 1:
                #     result = count*2

            return abs(result)


a = Solution().longestValidParentheses("()")
print(a)
