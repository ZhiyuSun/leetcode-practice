"""
字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。

S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。

返回任意一种符合条件的字符串T。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/custom-sort-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
# 2021.04.25 我的解法
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        dic = collections.defaultdict(int)
        for i in range(len(S)):
            dic[S[i]] = i
        return ''.join(sorted(list(T), key=lambda x: dic[x]))

# 2021.04.25 另一种巧妙的解法
class Solution1:
    def customSortString(self, S: str, T: str) -> str:
        # count[char] will be the number of occurrences of
        # 'char' in T.
        count = collections.Counter(T)
        ans = []

        # Write all characters that occur in S, in the order of S.
        for c in S:
            ans.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need
            # to write 'c' to our answer anymore.
            count[c] = 0

        # Write all remaining characters that don't occur in S.
        # That information is specified by 'count'.
        for c in count:
            ans.append(c * count[c])

        return "".join(ans)
