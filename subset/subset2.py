class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        self.subsetswithDupRecu(result,[],sorted(nums))
        return result
    def subsetswithDupRecu(self,result,cur,nums):
        if not nums:
            if cur not in result:
                result.append(cur)
        else:
            self.subsetswithDupRecu(result,cur,nums[1:])
            self.subsetswithDupRecu(result,cur+[nums[0]],nums[1:])
