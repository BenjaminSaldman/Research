import doctest


def safe_call(f, **kwargs):
    for i, j in kwargs.items():
        if i in f.__annotations__.keys():
            if f.__annotations__[i] != type(j):
                raise "Error"
    return f(**kwargs)


from queue import Queue
from stack import Stack

def breadth_first_search(start, end, neighbor_function):
    """
     >>> breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function)
     [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
     >>> breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=x_powers)
     [(0, 0), (1, 1), (2, 2)]
     The BFS code+path was taken from my project in OOP: https://github.com/BenjaminSaldman/Ex3-OOP/blob/master/src/GraphAlgo.py
     (Used with BFS and Shortest path)
     also used with https://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%92%D7%95%D7%A8%D7%99%D7%AA%D7%9D_%D7%97%D7%99%D7%A4%D7%95%D7%A9_%D7%9C%D7%A8%D7%95%D7%97%D7%91
     to get more ideas.
     """
    q = Queue()  # Queue to BFS algorithm
    path = []  # The path to return.
    parent = {}  # parent dict: key=node value=parent.
    visited = [start]  # all visited nodes.
    q.put(start)  # starting the scan with the first node.
    while not q.empty():
        x = q.get()
        if x == end:
            break
        for y in neighbor_function(x):
            if y not in visited:
                visited.append(y)
                q.put(y)
                parent[y] = x
    path.append(end)  # starting backtrace from the end.

    while path[len(path) - 1] != start:
        path.append(parent[path[len(path) - 1]])

    return path.reverse()  # we have to reverse the path so we can get: start->....->end


def four_neighbor_function(node):
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def x_powers(node):
    (x, y) = node
    return [(x ** 2 + 1, y ** 2 + 1)]


def three_neighbors(node):
    (x, y, z) = node
    return [(x + 1, y, z), (x - 1, y, z + 1), (x, y + 1, z - 1)]


print(breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function))
print(breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=x_powers))
print(breadth_first_search(start=(0, 0, 0), end=(2, 2, 2), neighbor_function=three_neighbors))

import doctest
from queue import Queue


def breadth_first_search(start, end, neighbor_function):
    """
     >>> breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function)
     [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
     >>> breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=x_powers)
     [(0, 0), (1, 1), (2, 2)]

     I used the pseudocode of BFS and dijkstra algorithm from wikipedia:
     https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
     https://en.wikipedia.org/wiki/Breadth-first_search
     Dijkstra is to construct the path and BFS to simulate dijkstra
     on unweighted graph.
     """
    q = Queue()  # Queue to BFS algorithm
    prev = {}  # parent dict: key=node value=parent.
    visited = [start]  # all visited nodes.
    q.put(start)  # starting the scan with the first node.
    while not q.empty():
        x = q.get()
        if x == end:
            break
        for y in neighbor_function(x):
            if y not in visited:
                visited.append(y)
                q.put(y)
                prev[y] = x
    S = []  # empty 'stack'.
    u = end  # current node .
    while u in prev:
        S.append(u)
        u = prev[u]
    S.append(start)
    seq = []  # path to return
    for i in range(len(S)):
        seq.append(S.pop())
    return seq


def four_neighbor_function(node):
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def x_powers(node):
    (x, y) = node
    return [(x ** 2 + 1, y ** 2 + 1)]


def three_neighbors(node):
    (x, y, z) = node
    return [(x + 1, y, z), (x - 1, y, z + 1), (x, y + 1, z - 1)]


# print(breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function))
# print(breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=x_powers))
# print(breadth_first_search(start=(0, 0, 0), end=(2, 2, 2), neighbor_function=three_neighbors))
# doctest.testmod(verbose=True)

x = {"a": 5, "c": [6, [4, 3, 5], 5], "b": [1, 3, 2, 4]}


def sort_dict(d):
    try:
        l = dict(d)
        l = sorted(l)
        ans = {}
        for i in l:
            ans[i] = d[i]
        return ans
    except:
        raise Exception


# def Check(d):
#     try:
#         iter(d)
#     except:
#         return
#     try:
#         if type(d)==dict:
#             d=sort_dict(d)
#             try:
#                 d[i] = sorted(d[i])
#             except:

def print_sorted(d):
    try:
        iter(d)
    except:
        return d
    try:
        if type(d) == dict:
            d = sort_dict(d)
            for i, j in d.items():
                try:
                    d[i] = sorted(d[i])

                except:
                    d[i] = print_sorted(d[i])
        else:
            d = sorted(d)
            for i in range(len(d)):
                try:
                    d[i] = sorted(d[i])

                except:
                    d[i] = print_sorted(d[i])

    except:
        if type(d) == dict:
            for i, j in d.items():
                d[i] = print_sorted(j)
        else:
            for i in range(len(d)):
                d[i] = print_sorted(d[i])

    return (d)


print(print_sorted(x))