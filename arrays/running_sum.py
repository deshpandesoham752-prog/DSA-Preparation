class Solution(object):
    def runningSum(self, nums):
       
             
             
             count=0
             result=[]
             for i in range (len(nums)):
                   count=count+nums[i]
                   result.append(count)
             return result  


