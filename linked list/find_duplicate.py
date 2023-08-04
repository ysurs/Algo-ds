to find duplicate in an array using constant extra space and without modifying the original array.

Input: nums = [1,3,4,2,2]
Output: 2

My approach:
    
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n=len(nums)
        count_array=[0]*n

        for i in nums:
            count_array[i]+=1
            if count_array[i]>1:
                return i