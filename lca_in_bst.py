# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
                
        # Approach: DFS on the root, ask at each level if curNode is LCA.
        def dfs(cur):
            # 3 Cases to consider from root:

            # 1. both p & q are in left subtree -> recurse on left
            if cur.val > p.val and cur.val > q.val:
                return dfs(cur.left)

            # 2. both p & q are in right subtree 
            elif cur.val < p.val and cur.val < q.val:
                return dfs(cur.right)

            # 3. p & q are in both subtrees
            else:
                return cur
        
        return dfs(root)
        