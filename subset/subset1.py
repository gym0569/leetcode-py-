class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[[]]
        for i in range(len(nums)):
            size=len(result)
            for j in range(size):
                result.append(list(result[j]))
                result[-1].append(nums[i])
        return result
