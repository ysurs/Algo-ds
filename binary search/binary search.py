Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        left=0
        right=n-1

        while left<=right:
            
            mid=(left+right)//2

            if nums[mid]==target:
                return mid

            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1

        
        return -1
    
points to note:

1. integer division
2. left<=right