class Solution:
    """
    就是以字符串中的每一个字符都当作回文串中间的位置，然后向两边扩散，
    每当成功匹配两个左右两个字符，结果 res 自增1，然后再比较下一对。
    注意回文字符串有奇数和偶数两种形式，如果是奇数长度，那么i位置就是中间那个字符的位置，所以左右两遍都从i开始遍历；
    如果是偶数长度的，那么i是最中间两个字符的左边那个，右边那个就是 i+1，这样就能 cover 所有的情况啦，而且都是不同的回文子字符串
    """
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        self.count = 0
        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i + 1)
        return self.count

    def helper(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
            self.count += 1