class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        分两步走：
        1） 将字符串整个翻转一遍
        2） 将字符串的每个单词识别出来，并翻转一遍
        """
        # reverse the whole string
        self.reverse(s, 0, len(s) - 1)

        # reverse each word
        self.reverse_word(s)

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    def reverse_word(self, s):
        n = len(s)
        start, end = 0, 0

        while start < n:
            # go to the end of the word
            while end < n and s[end] != ' ':
                end += 1

            # reverse the word
            self.reverse(s, start, end - 1)

            # move to the next word
            start = end + 1
            end += 1