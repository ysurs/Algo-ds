Remove Nth Node From End of List

1->2->3->4->5->6->7->8

remove 2nd node from end of list

output : 1->2->3->4->5->6->8


my approach:
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp=head
        length=0

        # length of ll
        while temp:
            length+=1
            temp=temp.next

        # will be position of node from start
        start_pos=length-n+1

        prev=None
        temp=head
        sub_len=0

        # removing node
        while temp:
            sub_len+=1
            if sub_len==start_pos:
                break
            prev=temp
            temp=temp.next
            
        if start_pos==1:
            return temp.next
        else:
            prev.next=temp.next
            return head

        return head
    

This solution does work, but it requires 2 passes to solve

Time complexity is O(n)

Following solution requires 1 pass to solve:
    
2 pointer approach:
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        left=dummy
        right=head

        while n:
            right=right.next
            n-=1
        
        while right:
            left=left.next
            right=right.next

        left.next=left.next.next

        return dummy.next
