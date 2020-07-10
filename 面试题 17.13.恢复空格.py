class Solution:
    def respace(self, dictionary: list, sentence: str):
        # new_str = ''
        # for d in dictionary:
        #     new_str += d
        # print(new_str)
        all_simple_index = {}

        for d in dictionary:
            for dd in d:
                simple_index = []
                for i in range(len(sentence)):
                    if sentence[i] == dd:
                        simple_index.append(i)
                print(dd, simple_index)
                all_simple_index.update({dd: simple_index})
        print(all_simple_index)
        # return  all_simple_index

        for d in dictionary:
            for dd in d:
                for i in all_simple_index.get(dd):


a = Solution().respace(["looked","just","like","her","brother"], "jesslookedjustliketimherbrother")
print(a)