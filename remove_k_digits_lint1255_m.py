class Solution:
    '''
    https://www.cnblogs.com/grandyang/p/8887985.html
    单调栈的一大优势就是线性的时间复杂度，所有的元素只会进栈一次，而且一旦出栈后就不会再进来了。
    单调递增栈可以找到左起第一个比当前数字小的元素。比如数组 [2 1 4 6 5]，最终栈内数字为 1，4，5。
    单调递减栈可以找到左起第一个比当前数字大的元素。

    可以使用单调栈。
    从高位向低位依次入栈，若当前数字小于栈顶元素且k不为0，则删除栈顶元素。
    最后将栈内的元素变为数字即可。
    '''

    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if k >= len(num):
            return '0'

        stack = []

        for i in range(len(num)):
            # k > 0 , 非空栈， 栈顶元素 > num[i]
            while len(stack) > 0 and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        if k != 0:  # 678, k=2  已经remove掉一些了
            final_stack = stack[:-k]
        else:
            final_stack = stack

        return ''.join(final_stack).lstrip('0') or '0'

