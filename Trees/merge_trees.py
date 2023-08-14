https://leetcode.com/problems/merge-two-binary-trees/description/

The approach i was trying to do:
    
class Solution:
def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:


	if not root1:

    if not root2:
        return
    if root1 and root2:
        value=root1.val+root2.val
    else:
        value=root1.val if root1 else root2.val
    
    newroot=TreeNode(value)
    
    mergeTrees(root1.left,root2.left)
    mergeTrees(root1.right,root2.right)
    
    
    
Efficient solution:

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return None

        v1=root1.val if root1 else 0
        v2=root2.val if root2 else 0

        newnode=TreeNode(v1+v2)

        newnode.left=self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        newnode.right=self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return newnode
    

Time complexity is O(n+m)
