"""
给你一个非空的字符串 s 和一个整数 k，你要将这个字符串中的字母进行重新排列，使得重排后的字符串中相同字母的位置间隔距离至少为 k。

所有输入的字符串都由小写字母组成，如果找不到距离至少为 k 的重排结果，请返回一个空字符串 ""。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rearrange-string-k-distance-apart
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import Counter

# 2021.04.26 有点难，思路难找
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not s or k <= 1: return s
        counter = Counter(s)
        a = list(map(list, counter.most_common()))
        c, t = a[0]
        if k *(t-1)+ sum([1 for c1, t1 in a if t1 == t]) > len(s): return ""
        temp = [[]for _ in range(t)]
        for i in range(t):
            for j, (c1, t1) in enumerate(a):
                if t1 == 0: continue
                temp[i].append(c1)
                a[j][1] -= 1
                if len(temp[i]) == k: break
        
        for i in range(t):
            for j, (c1, t1) in enumerate(a):
                if t1 == 0: continue
                temp[i].append(c1)
                a[j][1] -= 1
      
        res = ""
        for l in temp:
            res += "".join(l)

        return res


# 2021.04.26 民间解法，大顶堆的思路
from collections import deque
import heapq

class Solution1:
    def rearrangeString(self, s: str, k: int) -> str:
        s_hash = {}
        for c in s:
            s_hash[c] = s_hash.get(c, 0) + 1

        queue_assist = deque()
        heap_assist = []
        ans = ''

        for key, val in s_hash.items():
            heapq.heappush(heap_assist, (-val, key))

        while heap_assist:
            val, key = heapq.heappop(heap_assist)
            ans += key
            val += 1
            queue_assist.append((val, key))
            if len(queue_assist) >= k:
                duplicate_val, duplicate_key = queue_assist.popleft()
                if duplicate_val != 0:
                    heapq.heappush(heap_assist, (duplicate_val, duplicate_key))

        return ans if len(s) == len(ans) else ''