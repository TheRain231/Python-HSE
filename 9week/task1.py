"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        if arr == []:
            return None

        def create_bst(arrr):
            if arrr == [] or arrr is None:
                return
            elif len(arrr) == 1:
                return TreeNode(arrr[0])
            mid = len(arrr) // 2
            root = TreeNode(arrr[mid])
            root.left = create_bst(arrr[:mid])
            root.right = create_bst(arrr[mid + 1 :])
            return root

        return create_bst(arr)
