Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


approach 1:

1. inorder traversal of a valid bst is always strictly increasing.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # inorder traversal

        inorder=[]

        def dfs(root):
            if root==None:
                return
            
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        
        dfs(root)

        for i in range(1,len(inorder)):
            if inorder[i]<=inorder[i-1]:
                return False
        
        return True
    
Time complexity is O(n) and space complexity is O(n)

2. approach 2: using dfs

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        minvalue=float("-inf")
        maxvalue=float("inf")

        def dfs(root,minvalue,maxvalue):

            if root==None:
                return True
            
            if not(root.val>minvalue and root.val<maxvalue):
                return False
            
            return dfs(root.left, minvalue,root.val) and dfs(root.right,root.val,maxvalue)

        return dfs(root,minvalue,maxvalue)
    
    Time complexity is O(n) but space complexity is O(1)