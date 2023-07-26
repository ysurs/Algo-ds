Problem: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/?source=submission-ac


Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.


my approach: 
1. Couldn't figure out binary search
2. thought we have to take speeds from the dist array only but in reality it can range from 1 to 10**7
3. came up with a brute force approach as follows:

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        distance=sorted(dist)
        for i in distance:
            speed=i
            time=0
            found=True
            for idx,j in enumerate(dist):
                if idx!=len(dist)-1:
                    time+=math.ceil(j/speed)
                else:
                    time+=j/speed
                if time>hour:
                    found=False
                    break
            if found:
                return i
            
        return -1


actual answer:

class Solution:

    def find_time(self,mid,dist):
        time=0
        for idx,d in enumerate(dist):
            if idx!=len(dist)-1:
                time+=math.ceil(d/mid)
            else:
                time+=d/mid
        return time

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left=1
        right=10**7
        minspeed=float('inf')

        while left<=right:


            mid=(left+right)//2
            time=self.find_time(mid,dist)

            if time==hour:
                return mid

            elif time<hour:
                minspeed=min(minspeed,mid)
                right=mid-1
            else:
                left=mid+1


        if minspeed==float('inf'):
            return -1
        else:
            return minspeed

time complexity is o(nlogk)
space complexity is o(1)