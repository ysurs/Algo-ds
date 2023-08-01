
# given heads of 2 linked lists, we have to merge both the lists together resulting in a sorted linked list

1. my approach:

1. though of taking a single pointer and adding nodes to this new list as i compare the 2 linked lists
2. couldn't complete the solution due to lack of clarity and time limit.

Here is a good solution:

1. similar to my approach.
2. tested with a test case.
3. edge cases checked

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=cur=ListNode() # i forgot to add the brackets here. have to because instances of a class

        while list1 and list2:

            if list1.val<list2.val:
                cur.next=list1
                cur=list1
                list1=list1.next
            else:
                cur.next=list2
                cur=list2
                list2=list2.next
        
        if list1 or list2:
            cur.next=list1 if list2==None else list2

        return dummy.next
    

time complexity is O(N)
space complexity is O(1)