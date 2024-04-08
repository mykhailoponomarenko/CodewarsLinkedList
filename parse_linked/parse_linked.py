def linked_list_from_string(s):
#     if s.strip() == 'None' or s is None:
#         return Node(None)
    a = s.split(' -> ')
    if a[0] == 'None':
        return None
    b=[]
    for i in range(len(a)):
        if a[i].isdigit():
            b.append(int(a[i]))
        elif a[i].strip() == 'None':
            b.append(None)
        else:
            b.append(int(a[i].strip()))
    node = Node(b[0])
    b = b[1:]
    cur = node
    for i in b:
        if i is not None:
            cur.next = Node(i)
            cur = cur.next
        
    return node