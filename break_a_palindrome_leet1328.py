class Solution:
    """
    要点：
    1) 如果字符串长度为1，那么我们无论怎么修改最终都是回文，此时返回空。
    2) 理论上，我们需要将尽量靠前的字符修改成a，这样可以保证其字典顺序最小。
      但是如果靠前的字符已经是a，那么我们只能继续向后寻找首个不是a的字符，但是该字符位置不能是字符串的正中央，否则，修改后还是回文.
    3) 如果字符串所有字符均是a，那么应该将最后一位修改成b，这样可以保证字典顺序最小。
    """
    def breakPalindrome(self, palindrome):
        if not palindrome or len(palindrome) == 1:
            return ''
        p = list(palindrome)
        for i in range(len(p) //2):
            if p[i] != 'a':
                p[i] = 'a'
                return ''.join(p)
        p[-1] = 'b'
        return ''.join(p)