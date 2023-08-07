
We are given root of a binary tree, we have to invert it

Example:
    
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Approach: using depth first search for tree:
    
class Solution:
    def invert(self,root):
        if root==None:
            return 

        temp=root.left
        root.left=root.right
        root.right=temp

        self.invert(root.left)
        self.invert(root.right)

        return


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
    
    
    Points to note:
    
    1. be careful with the self pointer. I made the mistake of just calling invert without self. Its wrong because
    invert is the member of class Solution and hence it must be called using self.
    
    2. Complexity is O(n) and space is O(n) due to call stack