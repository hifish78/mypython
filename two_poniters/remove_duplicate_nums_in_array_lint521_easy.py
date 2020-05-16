class Solution:
    """
    这个问题有两种做法，第一种做法比较容易想到的是，把所有的数扔到 hash 表里，然后就能找到不同的整数有哪些。
    但是这种做法会耗费额外空间 O(n)。面试官会追问，如何不耗费额外空间。

    此时我们需要用到双指针算法，首先将数组排序，这样那些重复的整数就会被挤在一起。然后用两根指针，
    一根指针走得快一些遍历整个数组，另外一根指针，一直指向当前不重复部分的最后一个数。
    快指针发现一个和慢指针指向的数不同的数之后，就可以把这个数丢到慢指针的后面一个位置，并把慢指针++。

    感觉这道题其实算三指针了吧？一对前后比较用的指针，相差1 和一个result指针用来dump unique的数据。
    说双指针总觉得有些confused lol。

    """
    def deduplication(self, nums):
        if not nums:
            return 0
        data_dict, res = {}, 0
        for num in nums:
            if num not in nums:
                data_dict[num] = True
                nums[res] = num
                res += 1
        return res

    """
    感觉这道题其实算三指针了吧？一对前后比较用的指针，相差1 和一个result指针用来dump unique的数据。
    说双指针总觉得有些confused lol。
    """
    def deduplication2(self, nums):
        if not nums:
            return 0
        nums.sort()
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt
