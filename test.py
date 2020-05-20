from typing import List
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        left, right, longest = 0, 0, 0
        n = len(s)

        unique_char = {}
        while right < n:
            if s[right] in unique_char:
                # 下面两行是错误的，left只有在unique_char[s[right] 在窗口里（unique_dict[s[j]] >= i)
                # 才需要+1
                # left = max(left, unique_char[s[right]])
                # left += 1
                left = max(left, unique_char[s[right]])
            longest = max(longest, right - left + 1)
            unique_char[s[right]] = right + 1
            right += 1
        return longest

s = "abcb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))

# root = TreeNode(1)
# root.left = TreeNode(-5)
# root.right= TreeNode(3)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(-4)
# root.right.right = TreeNode(-5)


