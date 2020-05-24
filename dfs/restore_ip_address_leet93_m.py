class Solution:
    """
     首先我们要明确传统IP 地址的规律是分4个Part，每个Part是从0-255的数字0-255的数字，转换成字符，即每个Part可能由一个字符组成，二个字符组成，或者是三个字符组成。
     那这又成为组合问题了，dfs便呼之欲出所以我们写一个For循环每一层从1个字符开始取一直到3个字符，再加一个isValid的函数来验证取的字符是否是合法数字，
     如果是合法的数字，我们再进行下一层递归，否则跳过。
     注意开头如果是0的话要特殊处理，如果开头是0，判断整个串是不是0，不是的话该字符就是非法的。因为001，01都是不对的。
    """
    def restoreIpAddresses(self, s):
        if s is None:
             return None
        if len(s) == 0 or not s.isalnum():
            return []
        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, index, ip_list, res):
        # index: starting index
        if index == len(s) and len(ip_list) == 4:
            res.append('.'.join(ip_list))
            return
        # if index == len(s) but len(ip_list) ! = 4 or index != len(s) but len(ip_list) == 4
        if index == len(s) or len(ip_list) == 4:
            return

        # try the current position
        for i in range(1, 4):
            if index + i <= len(s) and self.isValid(s[index : index + i]):
                ip_list.append(s[index: index + i])
                self.dfs(s, index + i, ip_list, res)
                ip_list.pop()

    def isValid(self, str):
        if str[0] == '0' and len(str) > 1:
            return False
        return 0 <= int(str) <= 255

str = '25525511135'
sol = Solution()
sol.restoreIpAddresses(str)
