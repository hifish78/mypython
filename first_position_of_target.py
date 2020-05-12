class Solution:
    """
    二分法模板：(14, 457, 458)
    1) Since we are using “start+1 < end”, so 循环退出的时候要check START & END 点
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end

    2) Since we find the first position, check nums[start] first. If we find the last position, check nums[end] first

    3) About nums[mid] == target 归类到 start = mid or end = mid ?
    如果找1st position, 我们应该还需要往左边找，因为左边有更小的INDEX的可能， 所以
    if nums[mid] == target:
        end = mid
    elif nums[mid] < target:
        start = mid
    else:
        end = mid

    4) About start < end or start + 1 < end
       if using start < end; one example [1,1], target = 2;  mid is always equal to start, infinitive loop!!!
       Since we are using “start + 1 < end”, we missed start point & end point
       (one example is: [1,1], target = 1; start = 0; end = 1; start + 1 < end always false, skip the loop,
       but actually we have expected position for “1”, so need to check start & end point.
       that’s why we have the last 2 statements.

    """
    def binarySearch(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) -1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1