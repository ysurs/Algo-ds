https://leetcode.com/problems/reorder-list/description/

If the the list is 1->2->3->4, then reorder list such that it becomes 1->4->2->3

My approach:

1. Put nodes of linked list into a stack 
2. traverse the original list and pop the top of stack.
3. make a new list 
4. also maintain a set with seen nodes

Did not fully implement it.


Efficient approach:

1. Maintain a slow and fast pointer
2. Find the mid point of the list using slow and fast pointer
3. reverse the second half of the list
4. merge the first half and the second half.

Note: Do not over complicate the naming of variables, no harm in using temp, prev etc 

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        prev=slow.next=None

        # reversing the ll
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt

        
        # merging the two lists
        first,second=head,prev

        while second:
            tmp1=second.next
            tmp2=first.next
            first.next=second
            second.next=tmp2
            first=tmp2
            second=tmp1

        return head
    
    Time complexity is O(n) and space is O(1)
