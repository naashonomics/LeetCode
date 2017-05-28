#Given a binary tree, return the inorder traversal of its nodes' values.

#For example:
#Given binary tree [1,null,2,3],
#TC O(n) SC (1)
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
   
        if root == None:
            return []
        else:
            result = []
            stack = []
            node = root
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    result.append(node.val)
                    node = node.right
            return result
