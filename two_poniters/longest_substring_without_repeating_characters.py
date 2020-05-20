class Solution:
    """
    Sliding Window1:
    To check if a character is already in the substring, we can use set as a sliding window
    check if a character in the current can be done in O(1)
    We use set to store the characters in current window [i, j), (j = i initially).
    Then we slide the index j to the right. If it is not in the Set, we slide j further.
    Doing so until s[j] is already in the Set.
    At this point, we found the maximum size of substrings without duplicate characters
    start with index i. If we do this for all i, we get our answer.
    """

    # Time complexity : O(2n) = O(n).
    # In the worst case each character will be visited twice by i and j.

    # Space complexity : O(min(m, n)). Same as the previous approach.
    # We need O(k) space for the sliding window, where k is the size of the Set.
    # The size of the Set is upper bounded by the size of the string n and
    # the size of the charset/alphabet m.
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        longest, i, j = 0, 0, 0
        unique_set = set()
        n = len(s)
        while i < n and j < n:
            if s[j] not in unique_set:
                unique_set.add(s[j])
                longest = max(longest, j - i + 1)
                j += 1
            else:
                unique_set.remove(s[i])
                i += 1
        return longest

    """
    The above solution requires at most 2n steps. 
    In fact, it could be optimized to require only n steps. 
    Instead of using a set to tell if a character exists or not, 
    we could define a mapping of the characters to its index. 
    Then we can skip the characters immediately when we found a repeated character.
    
    The reason is that if s[j] have a duplicate in the range [i, j) with index j', 
    we don't need to increase ii little by little. 
    We can skip all the elements in the range [i, j'] and let i to be j' + 1 directly.
    """

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        longest, i, j = 0, 0, 0
        # define a mapping of characters to its index
        unique_dict = {}
        n = len(s)
        while j < n:
            if s[j] in unique_dict:
                # i只有在unique_char[s[j] 在窗口里（unique_dict[s[j]] >= i) 才需要做处理
                # 挪到相同字符的后一个位置 unique_dict[s[j]] + 1
                if unique_dict[s[j]] >= i:
                    i = unique_dict[s[j]] + 1
            longest = max(longest, j - i + 1)
            unique_dict[s[j]] = j
            j += 1
        return longest


sol = Solution()
s = 'abcb'
print(sol.lengthOfLongestSubstring(s))

