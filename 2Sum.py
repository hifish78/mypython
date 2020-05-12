class Solution(object):
    """
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



# sol = Solution()
# nums = [2,7,11,15]
# target = 9
# print(sol.twoSum(nums, target))