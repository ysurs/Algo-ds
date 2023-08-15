Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


My approach:
    
Wrong:
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        running_sum=0
        is_present=False

        if root==None:
            return False


        def dfs(root,running_sum,target_sum):
            nonlocal is_present
            if root==None:
                if running_sum==target_sum:	
                    is_present=True
                    return
            else:
                if not is_present:
                    running_sum+=root.val
                    dfs(root.left,running_sum,target_sum)
                    dfs(root.right,running_sum,target_sum)
            return
				
        dfs(root,running_sum,targetSum)
        return is_present
    

Correct solution:
    
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        running_sum=0
        
        def dfs(node,running_sum):
            if not node:
                return False
            
            running_sum+=node.val

            if node.left==None and node.right==None:
                if running_sum==targetSum:
                    return True
            
            return dfs(node.left,running_sum) or dfs(node.right,running_sum)
        
        return dfs(root,running_sum)

