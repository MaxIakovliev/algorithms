# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    https://leetcode.com/problems/check-completeness-of-a-binary-tree/
    """
    def isCompleteTree(self, root: 'TreeNode') -> bool:
        queue=list()
        queue.append(root)
        end=False
        while len(queue)!=0:
            cur=queue.pop(0)
            if cur is None:
                end=True
            elif end ==True:
                return False
            else:
                queue.append(cur.left)
                queue.append(cur.right)
        return True



            
            
                

        