
To find the right view of a binary tree: https://leetcode.com/problems/binary-tree-right-side-view/description/


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=collections.deque([root])
        result=[]
        

        while q:   ## while queue is non empty
            rightnode=None
            q_length=len(q)
            for i in range(q_length):
                node=q.popleft()
                if node:
                    rightnode=node
                    q.append(node.left)
                    q.append(node.right)
            if rightnode:
                result.append(rightnode.val)


        return result


Time and space complexity is O(n)

The space complexity depends on the maximum number of nodes that can be present at any level in the queue.
In the worst case, when the binary tree is a complete binary tree, the maximum number of nodes in a level is 2**h,
where h is height of the tree.

it will be o(2**h) but h is log n base 2 where n is the number of nodes. Hence space complexity is o(n)