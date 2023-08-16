Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

Approach:
1. use the property of bst
2. if the current node has value greater than both the nodes, no point in searching on the right side 
3. the first node where its value is less than 1 node and greater than the other is the lca

iterative solution:

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        cur=root

        while cur:
            if cur.val>p.val and cur.val>q.val:
                cur=cur.left
            elif cur.val<p.val and cur.val<q.val:
                cur=cur.right
            else:
                return cur

time complexity is O(log(n)) and space is O(1)


recursive:
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root

time complexity is O(log(n)) and space is O(log(n))