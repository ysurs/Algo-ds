To perform level order traversal of tree:
    
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        q=collections.deque([root])
        level_order=[]

        while q:
            q_length=len(q)
            level_nodes=[]
            for i in range(q_length):
                node=q.popleft()
                if node:
                    level_nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level_nodes:                            # Important condition, otherwise will give error
                level_order.append(level_nodes)

        return level_order