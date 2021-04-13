"""
这个问题是 LeetCode 平台新增的交互式问题 。

我们给出了一个由一些独特的单词组成的单词列表，每个单词都是 6 个字母长，并且这个列表中的一个单词将被选作秘密。

你可以调用 master.guess(word) 来猜单词。你所猜的单词应当是存在于原列表并且由 6 个小写字母组成的类型字符串。

此函数将会返回一个整型数字，表示你的猜测与秘密单词的准确匹配（值和位置同时匹配）的数目。此外，如果你的猜测不在给定的单词列表中，它将返回 -1。

对于每个测试用例，你有 10 次机会来猜出这个单词。当所有调用都结束时，如果您对 master.guess 的调用不超过 10 次，并且至少有一次猜到秘密，那么您将通过该测试用例。

除了下面示例给出的测试用例外，还会有 5 个额外的测试用例，每个单词列表中将会有 100 个单词。这些测试用例中的每个单词的字母都是从 'a' 到 'z' 中随机选取的，并且保证给定单词列表中的每个单词都是唯一的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/guess-the-word
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.13 直奔题解

class Solution:
    def findSecretWord(self, wordlist, master):
        def distance(x,y):
            ans = 0
            for i in range(6):
                if x[i] == y[i]:
                    ans += 1
            return ans
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        dp = [0] * len(wordlist) #记录是否被排除
        for g in range(10):
            #寻找下一个猜测单词
            candidate = 0
            vote = float('inf')
            for i in range(len(wordlist)):
                if dp[i] == 0:
                    dis = [0] * 7
                    for j in range(len(wordlist)):
                        if j != i and dp[j] == 0:
                            dis[distance(wordlist[i],wordlist[j])] += 1
                    if max(dis) < vote:
                        candidate = i
                        vote = max(dis)
            #猜测
            dp[candidate] = 1
            tmp = master.guess(wordlist[candidate])
            #排除不可能的单词
            for i in range(len(wordlist)):
                if dp[i] == 0 and distance(wordlist[candidate],wordlist[i]) != tmp:
                    dp[i] = 1
