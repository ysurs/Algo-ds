Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # root will always be a good node
        # we have to reach every node

        result=[]
        pathmax=float("-inf")

        def dfs(root,pathmax):

            if root==None:
                return
            
            if root.val>=pathmax:
                result.append(root.val)
                pathmax=root.val
            
            dfs(root.left,pathmax)
            dfs(root.right,pathmax)
            return
        
        dfs(root,pathmax)

        return len(result)
    
points:

1. maintain the maximum in each path and compare current node while performing dfs with max in the path. 
2. If current value is greater than max value till now then current node is good.

Time complexity is O(n)
space complexity is O(n) due to call stack