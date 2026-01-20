# linked list :
# Concept: A Linked List is like a train.

# Each bogie is called a Node.
# Each Node has Data and a Next (link to the next bogie).
# The first bogie is called Head.
# The last bogie points to None (no next bogie).
# Why Linked List?
# Dynamic Size: Linked Lists can grow and shrink in size.
# Efficient Insertions/Deletions: Adding or removing nodes is easier.
# Types of Linked Lists:
# Singly Linked List: Nodes link to the next node only.
# Doubly Linked List: Nodes link to both next and previous nodes.
# Circular Linked List: Last node links back to the head.
# Basic Operations:
# Traversal: Visit each node in the list.
# Insertion: Add a new node at the beginning, end, or specific position.
# Deletion: Remove a node from the beginning, end, or specific position.
# Searching: Find a node with a specific value.
# Implementation in Python:

# Creating a Node Class
# Task: Define a class Node that stores data and next.
# Input: 10.
# Output: A node object containing 10.

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

head = Node(10)
second = Node(20)
last = Node(30)
print("Node data:", head.data)
print("Node data:", second.data)
print("Node data:", last.data)

head.next = second
second.next = last
last.next = None
print("Head points to:", head.next.data)
print("Second points to:", second.next.data)
print("Last points to:", last.next)

# Traversing (Printing) the List
# Task: Write a while loop to go through the list and print all data.

while head is not None:
    print(head.data, end=" -> ")
    head = head.next
