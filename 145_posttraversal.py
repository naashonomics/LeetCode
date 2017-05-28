# O(n) TC O(1) SC 


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        else:
            stack = []
            out_stack = []
            stack.append(root)
            while stack != []:
                current = stack.pop()
                out_stack.append(current.val)
                if current.left != None:
                    stack.append(current.left)
                if current.right != None:
                    stack.append(current.right)

            return out_stack[::-1]  
