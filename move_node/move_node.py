class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    

    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
    
def move_node(source, dest):
    print(source)
    print(dest)
    if not source:
        raise ValueError
    if dest is None:
        if not source.next:
            return Context(None, Node(source.data))
        return Context(source.next, Node(source.data))

    d = Node(source.data)
    d1 = dest
    d2 = dest.data
#     if not dest:
#         return Context(source.next, source)
    # Your code goes here.
    # Remember to return the context.
    s1=source.next
#     if dest:
    d.next = d1
    return Context(s1, d)