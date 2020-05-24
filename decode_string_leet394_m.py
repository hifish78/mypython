class Solution:
    '''
    要点：
    1） 看到括号匹配的题肯定想到用栈去做。
    2） 这个题，遇到’[‘就把之前的字符串进行进栈操作。遇到’]'进行出栈操作。
    3） curstr保存的是出栈操作完成后的字符串。
    4） 注意这一步：curstr = prestr + prenum * curstr，
        prestr是前面的字符串，prenum * curstr是这一步骤结束之后的字符串，所以是前面的字符串+现在的字符串得到目前已有的字符串。
    '''
    def decodeString(self, s: str) -> str:
        stack = []
        curnum = 0
        curstr = ''

        for i in range(len(s)):
            if s[i].isdigit():
                curnum = curnum * 10 + int(s[i])
            elif s[i] == '[':
                stack.append(curstr)
                stack.append(curnum)
                curnum = 0
                curstr = ''
            elif s[i] == ']':
                prenum = stack.pop()
                prestr = stack.pop()
                curstr = prestr + prenum * curstr
            else:
                curstr = curstr + s[i]

        return curstr

s = '3[a2[c]]'
sol = Solution()
print(sol.decodeString(s))