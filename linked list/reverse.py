
The problem is related to reversing a linked list

input : 1->2->3->4
output: 4->3->2->1

my approach:

1. I was 2 pointers, one equal to head and other equal to head.next
2. This approach made things complicated and i made mistake

better solution: iterative:

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous=None
        current=head

        while current:
            next=current.next
            current.next=previous
            previous=current
            current=next
        
        return previous
    
time complexity is O(n), space complexity is O(1)


recursive:
    
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        new_head=head
        
        if head.next:
            new_head=self.reverseList(head.next)
            head.next.next=head
        head.next=None
        return new_head

time complexity is O(n), space complexity is O(n)

1. In recursive case, we reach the last node and assign it as our new head
2. Take an example and dry run on this solution.