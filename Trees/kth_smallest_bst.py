Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


1. approach 1: recursive inorder traversal of bst gives sorted array

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=[]

        def dfs(root):

            if root==None:
                return
            
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
            return
        
        dfs(root)

        return result[k-1]


Time complexity is O(n) and space complexity is O(n)

2. iterative approach:
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        n=0

        cur=root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            
            cur=stack.pop()
            n+=1
            if n==k:
                return cur.val
            
            cur=cur.right