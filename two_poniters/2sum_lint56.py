class Solution(object):
    """
    dict方法使用一个dictionary结构来记录对应的数字是否出现，以及其下标。
    时间复杂度为O(n)。空间上需要开辟dictionary来存储, 空间复杂度是O(n)。

    key:value --> nums[i]: i
    get all of items from dict: dict.items() , it is a list of tuple as element
    get all of keys from dict: dict.keys()
    get all of values from dict: dict.values()

    data[other] <=> data.get(other)

    enumerate 使用 enumerate(iterable, start=0)
    l1 = ["eat","sleep","repeat"]
    e1 = enumerate(l1)
    print(e1)
    <enumerate object at 0x10d210870>
    print(list(e1))
    [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

    >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons, start=1))       # 下标从 1 开始
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

    >>>i = 0
    >>> seq = ['one', 'two', 'three']
    >>> for element in seq:
    ...     print i, seq[i]
    ...     i +=1
    ...
    0 one
    1 two
    2 three
    """
    def twoSum(self, nums, target):
        dictionary = {}
        for i in range(len(nums)):
            if target - nums[i] in dictionary.keys():
                return [dictionary.get(target- nums[i]), i]
            else:
                dictionary[nums[i]] = i
        return [-1, -1]

    def twoSum1(self, nums, target):
        data = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in data:
                return [data.get(other), i]
            else:
                data[num] = i
        return [-1, -1]

    ## 如果是返回两个数而不是数组下标，可以用双指针来做
    # 首先我们对数组进行排序。用两个指针(L, R)
    # 从左右开始：
    # 如果numbers[L] + numbers[R] == target, 说明找到，返回对应的数。
    # 如果numbers[L] + numbers[R] < target, 此时L指针右移，只有这样才可能让和更大。
    # 反之使R左移。L和R相遇还没有找到就说明没有解。
    # Two pointers方法，基于有序数组的特性，不断移动左右指针，减少不必要的遍历，时间复杂度为O(nlogn), 主要是排序的复杂度。
    # 但是在空间上，不需要额外空间，因此额外空间复杂度是 O(1)
    def twoSum2(self, nums, target):
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [nums[l], nums[r]]
            if nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        return []

# sol = Solution()
# nums = [2,7,11,15]
# target = 9
# print(sol.twoSum(nums, target))