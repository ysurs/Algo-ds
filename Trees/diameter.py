We are given the root. We need to find the diameter of a binary tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res=0

        def dfs(root):
            nonlocal res
            
            if root==None:
                return -1
            
            lh=dfs(root.left)
            rh=dfs(root.right)

            diameter=2+lh+rh
            res=max(res,diameter)

            return 1+max(lh,rh)

        dfs(root)
        return res
    
Points to note:
1. This is dfs using recursion.
2. To find diameter, we need left height and right height. Where height of a node is the number of edges in the longest path 
from it to a leaf node.
3. Height of leaf nodes is 0 and the diameter will also be zero so -1 is used in base case.
4. Complexity if O(n) and space complexity is O(n)