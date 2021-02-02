def search(node):
    if check[node] == 1:
        return
    if check[parentnode[node]] != 1:
        childnode[parentnode[node]] = node
        return
    check[node] = 1

    for i in graph[node]:
        search(i)
    if childnode[node]:
        search(childnode[node])

def solution(n, path, order):
    global check, room_count, visit_room, parentnode, childnode, graph
    visit_room = 0
    room_count = n

    graph = [[] for _ in range(n)]
    check = [0 for _ in range(n)]
    check[0] = 1
    parentnode = [0 for _ in range(n)]
    childnode = [0 for _ in range(n)]

    for room1, room2 in path:
        graph[room1].append(room2)
        graph[room2].append(room1)
    for pre_visit, next_visit in order:
        if parentnode[next_visit] != 0:
            return False
        parentnode[next_visit]=pre_visit

    if parentnode[0] != 0:
        return False

    for i in graph[0]:
        search(i)

    for i in range(room_count):
        if check[i] == 1:
            visit_room += 1
    if visit_room == room_count:
        return True
    else:
        return False