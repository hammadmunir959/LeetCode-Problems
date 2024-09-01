# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

class Linkedlist :
    def __init__(self) -> None:
        self.head = None

    def insertion(self, data):
        new_Node = Node(data)

        if self.head == None:
            new_Node = self.head
            self.head = new_Node

class Solution:
    def mergeTwoLists(self, L_list1, L_list2) :
        

        



list1 = [1,2,4]

list2 = [1,3,4]

problem = Solution()

problem.mergeTwoLists(list1, list2 )



        