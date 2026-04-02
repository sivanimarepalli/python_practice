# Given the root of a binary tree, return the postorder traversal of its nodes' values.

#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        post_list=[]
        if root is None:
            return []
        post_list.extend(self.postorderTraversal(root.left))
        post_list.extend(self.postorderTraversal(root.right))
        post_list.append(root.val)
        return post_list
        