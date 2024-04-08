from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    a = Node(data)
    a.next = head
    return a

def build_one_two_three():
    a = None
    a = push(a, 3)
    a = push(a, 2)
    a = push(a, 1)
    return a