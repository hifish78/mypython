class Solution:
    #     def reverseWords(self, s: str) -> str:
    #         if not s:
    #             return s

    #         parts = s.split()
    #         str_list = list()
    #         for i in range(len(parts) - 1, -1, -1):
    #             part = parts[i].strip()
    #             str_list.append(part)

    #         return ' '.join(str_list)

    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))