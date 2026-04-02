# Given the root of a binary tree, return the preorder traversal of its nodes' values.

#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre_list=[]
        if root is None:
            return []
        pre_list.append(root.val)
        pre_list.extend(self.preorderTraversal(root.left))
        pre_list.extend(self.preorderTraversal(root.right))
        return pre_list
        