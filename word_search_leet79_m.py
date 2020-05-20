class Solution:
    """
    对matrix进行搜索，当第一个字符匹配上之后，再看下一个字符。
    每次对当前位置的上下左右四个方向进行搜索，有一个满足即返回true。
    在对当前位置的邻接位置搜索之前，用"#"覆盖当前位置的值，这样在新的搜索时不会取到之前取过的重复位置，避免重复。
    当四个方向均不满足时，将当前位置恢复为原来值，然后对当前位置进行新的搜索。

    Time Complexity: O(N* 4^L). N is the number of celss in the board and L is the length of the word to be matched
    Space Complexity:O(L) where L is the length of the word to be  matched.
    The main consumption of the memory lies in the recursion call of the backtracking function.
    The maximum length of the call stack would be the length of the word.
    """
    def exist(self, board, word):
        # 排除len(board) == 0 or board = [] 情况
        if not board:
            return False
        if not word:
            return True
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.findWord(i, j, board, word, 0):
                    return True
        return False
    #start 代表新搜索开始的位置，当和WORD长度相等的时候，表示WORD中所有字符均已匹配
    def findWord(self, i, j, board, word, start):
        if start == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[start]:
            return False

        board[i][j] = '#'
        if self.findWord(i - 1, j, board, word, start + 1) or \
            self.findWord(i + 1, j, board, word, start + 1) or \
            self.findWord(i, j - 1, board, word, start + 1) or \
            self.findWord(i, j + 1, board, word, start + 1):
            return True
        board[i][j] = word[start]
        return False

sol = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = 'SEE'
sol.exist(board, word)
