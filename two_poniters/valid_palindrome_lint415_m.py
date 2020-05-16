class Solution:
    """
    同向双指针的典型应用。
    Python functions:
    isalnum(), isdigit(), isalpha()
    >>> 'a1'.isalpha()
    False
    >>> 'a1'.isdigit()
    False
    >>> 'a1'.isalnum()
    True
    s.upper(), s.lower(), s.count('is'), s.find('this'), s.replace("to", "three")
    >>> s = 'that that is is a book'
    >>> s.count('is')
    2
    """
    def isPalindrome(self, s):
        i, j = 0 , len(s) - 1
        while i < j:
            # 容易出错的地方，下一行必须要加 while i < j
            # one corner case: '.,' , 会出现string index out of range
            # if the statement is : while not s[i].isalnum()
            # while i< j and not s[i].isdigit() and not s[i].isalpha()): <=>
            # while i < j and not s[i].isalnum()
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
        return True