Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l=0
        r=len(nums)-1
        res=nums[0]

        while l<=r:
            if nums[l]<nums[r]:
                return min(res,nums[l])
                
            mid=(l+r)//2
            res=min(res,nums[mid])

            if nums[mid]>=nums[l]:
                l=mid+1
            else:
                r=mid-1

        return res
    
Points to note:

1. If an array is already sorted and not rotated, we need to find the min of value at l and current result.
2. if mid element is greater than left that means we have to move to right given than its rotated because all element to right will 
be less than all elements to left of mid.
3. if mid element is less than left that means we have to move to left to search for a possibility of lower element.