Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Pointers:
    
1. Always draw the diagram for a simple test case first and then a complex test case. 

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val!=q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
    
    Time complexity is O(n+m) where n is the number of nodes in the first tree and m is the number of nodes in the second.
    Same is the space complexity