Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


My approach:

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root==None and subRoot==None:
            return True

        if root==None and subRoot!=None:
            return False
        
        if root==subRoot:
            return self.isSubtree(root.left,subRoot.left) or self.isSubtree(root.right,subRoot.right)
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            
            
I was thinking in the right direction and I realised the mistake in my code. The answer was to make separate functions like below:

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot==None:
            return True
        if root==None:
            return False
        if self.issame(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        

    def issame(self,r,sr):
        if r==None and sr==None:
            return True
        if r==None or sr==None:
            return False
        if r.val!=sr.val:
            return False
        return self.issame(r.left,sr.left) and self.issame(r.right,sr.right)
        
        
Time complexity is O(n*m) where n is the number of nodes in the first tree and m is the number of nodes in the second tree.