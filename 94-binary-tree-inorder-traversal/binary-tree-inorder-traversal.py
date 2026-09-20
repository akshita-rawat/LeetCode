class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root
        
        while curr or stack:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process the current node
            curr = stack.pop()
            result.append(curr.val)
            
            # Move to the right subtree
            curr = curr.right
            
        return result
