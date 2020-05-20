class Solution:
    """
    1) find candidate by one pass: (make sure other people are not a celebrity)
       首先loop一遍找到一个人i使得对于所有j(j>=i)都不认识i。
       knows(i, j): by comparing a pair(i, j), we are able to discard one of them
       if knows(i,j): i is guaranteed not to be celebrity
       otherwis: j is not a celebrity
    2) make sure if the candidate is a celebrity by one pass
       然后再loop一遍判断是否有人不认识i或者i认识某个人。
    """
    def findCelebrity(self, n):
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        for i in range(n):
            if candidate != i and knows(candidate, i):
                return -1
            if candidate !=i and not not knows(i, candidate):
                return -1
        return candidate