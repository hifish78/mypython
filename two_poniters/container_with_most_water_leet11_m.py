class Solution:
    '''
    要点： height[left] or height[right]应该舍弃谁？
    左右指针向中间移动的话，要求面积最大，向中间移动边已经减少了，所以必须想着
    指针移动的话高度要增加，所以应该舍弃height[left] , height[right]中值小的那个
    https://www.youtube.com/watch?v=IONgE6QZgGI
    '''
    def maxArea(self, height):
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            res = max(res, h * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res