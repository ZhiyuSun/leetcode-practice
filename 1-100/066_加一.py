class Solution:
    def plusOne(self, digits):
        a = ''
        for i in digits:
            a += str(i)
        return list(map(int, str(int(a)+1)))
