# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        queue = [root]
        visited = []

        while (len(queue) > 0):
            queue_length = len(queue)
            level = []

            for i in range(queue_length):

                curr = queue[0]
                level.append(curr.val)

                if curr.left != None:
                    queue.append(curr.left)
                
                if curr.right != None:
                    queue.append(curr.right)

                queue.pop(0)

            if level != []:
                visited.append(level)

        return visited