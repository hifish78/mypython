class Solution:
    # Solution1: item is [] + append + pop
    # exit criteria: len(item) == len(digits) or index == len(digits)
    def letterCombinations(self, digits):
        if not digits:
            return []
        self.keyboard = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        self.dfs(digits, 0, [], res)
        return res

    def dfs(self, digits, index, item, res):
        if len(item) == len(digits):
            res.append(''.join(item))
            return
        for ch in self.keyboard[digits[index]]:
            item.append(ch)
            self.dfs(digits, index + 1, item, res)
            item.pop()

    # Solution2: 直接在字符串上操作,
    # 退出条件： len(digits) == index or index == len(digits)
    def letterCombinations2(self, digits):
        if not digits:
            return []
        self.keyboard = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        self.dfs2(digits, 0, '', res)
        return res

    def dfs2(self, digits, index, item, res):
        if len(digits) == index:
            res.append(item)
            return

        for ch in self.keyboard[digits[index]]:
            self.dfs(digits, index + 1, item + ch, res)


