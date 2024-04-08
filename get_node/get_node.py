from preloaded import Node

def get_nth(node, index):
    cur = node
    ind = 0
    while cur is not None and ind != index:
        cur = cur.next
        ind += 1
    if cur is None:
        raise IndexError("Index out of range")
    return cur