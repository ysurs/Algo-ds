We have to find the max depth of a binary tree. Max depth is the number of nodes in the longest path from the root to the leaf nodes.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Points to remember:
1. I forgot to write : maxdepth=self.depth(root.left,depth,maxdepth) and it was giving me error
2. Time complexity is O(n)

class Solution:
    def depth(self,root,depth,maxdepth):
        if root==None:
            maxdepth=max(maxdepth,depth)
            return maxdepth
        depth+=1
        maxdepth=self.depth(root.left,depth,maxdepth)
        maxdepth=self.depth(root.right,depth,maxdepth)
        return maxdepth
	
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth=0
        maxdepth=0
        return self.depth(root,depth,maxdepth)