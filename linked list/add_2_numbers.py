We have to add 2 non negative numbers without any leading zeros given in reverse order

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

my approach:
    class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tmp1=l1
        tmp2=l2

        counter=0

        tmp_new=None
        new_head=None
        value=0
        carry=0


        while tmp1 and tmp2:
            total=tmp1.val+tmp2.val+carry
            value=(total)%10
            carry=(total)//10
            if counter==0:
                new_head=ListNode(value,None)
                tmp_new=new_head
                counter+=1
            else:
                tmp_new.next=ListNode(value,None)
                tmp_new=tmp_new.next
            tmp1=tmp1.next
            tmp2=tmp2.next


        while tmp1:
            total=tmp1.val+carry
            value=(total)%10
            carry=total//10
            tmp_new.next=ListNode(value,None)
            tmp_new=tmp_new.next
            tmp1=tmp1.next




        while tmp2:
            total=tmp2.val+carry
            value=(total)%10
            carry=total//10
            tmp_new.next=ListNode(value,None)
            tmp_new=tmp_new.next
            tmp2=tmp2.next
        
        if carry:
            tmp_new.next=ListNode(carry,None)
            tmp_new=tmp_new.next


        return new_head
    
    
    Points to remember:
    
    1. Missed the last edge case when 2 linked lists are of same length and we have a carry. Add the following also to handle it:
        if carry:
            tmp_new.next=ListNode(carry,None)
            tmp_new=tmp_new.next
    
    2. Made a couple of mistakes of not using correct pointers in loops like instead of tmp1 in while loop, was using l1
    3. Since we are looking for integers, forgot the // division
    4. Was forgetting tmp1=tmp1.next in while loops - leading to memory exceeded
    
    
    More concise way of doing:
        
    
        # Will be the head node of new list
    class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()
        current=dummy

        carry=0

        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            val=val1+val2+carry
            carry=val//10
            current.next=ListNode(val%10)
            
            current=current.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        
        return dummy.next