class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def stringify(node):
    data = []
    while node is not None:
        data.append(str(node.data))
        node = node.next
    data.append('None')
    return ' -> '.join(data)
    