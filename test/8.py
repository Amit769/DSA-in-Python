#lowest common ancestor of a binary tree
class solution:
    def tree(self, root, p, q):
        
        if root is None:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.tree(root.left, p, q)
        right = self.tree(root.right, p, q)
        
        if left and right:
            return root
        
        elif left:
            return left
        
        else:
            return right 
    
    
    
    
    
    