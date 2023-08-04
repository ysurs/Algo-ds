To check if a linked list has cycle:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

1. My approach:

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow=head
        fast=head.next


        while fast!=None or fast.next!=None:
            if fast==slow:
                break
            fast=fast.next.next
            slow=slow.next


        if fast==None or fast.next==None:
            return False
        else:
            return True

This will give run time error because:

1. both conditions will be checked so if fast==None then fast.next will be wrong
2. i also missed the case when head==None, in that case head.next will be wrong.

Improved solution:

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        slow=head
        fast=head.next


        while fast!=None:
            if fast==slow:
                break
            fast=fast.next.next if fast.next else None
            slow=slow.next


        if fast==None:
            return False
        else:
            return True
        
Time complexity: O(N)