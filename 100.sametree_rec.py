#Given two binary trees, write a function to check if they are equal or not.
#Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

#Divide and conquer(Recursion), time complexity = O(n),
#n is the number of nodes,
                                        
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if(p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)):
                return True
        return False
