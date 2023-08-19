You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.


1. Start with regular binary search.
2. check if mid element is different from its neighbors, if true, return the mid element.
3. It important to check edge cases in point 2, element at the extremities and hence the extra conditions.
4. importance to be given to positioning of or and and conditions. 


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            mid=l+(r-l)//2

            if (mid-1<0 or nums[mid-1]<nums[mid]) and (mid+1==len(nums) or nums[mid+1]>nums[mid]):
                return nums[mid]

            leftarray=mid-1 if nums[mid-1]==nums[mid] else mid

            if leftarray%2==1:
                r=mid-1
            else:
                l=mid+1

