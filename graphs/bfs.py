'''
Breadth First Search

Explores a graph looking at each neighbor of a node before it iterates
to the next level neighbors.

Graph Representation - Adjacency List:
  Array of length |V|
  for every vertex, Adj[u] stores u's neighbors.

Adjacenty List is great for graph exploration.


Implemention of Adjacency List:
  Multiple Uses:
  - Array. At adj[u] the array points to a linked list
  - Hash Table. Look up key adj[u] points to a list of neighbors.

  Single Uses:
  - Object Oriented. Each Vertex is an object so
      v.neighbors = [list of neighbors]

  Implicit Representation:
    - Adj[u] is a function (generates the vertices)
    - v.neighbors() is now a method call
'''



def bfs(adj, start):
  level = { start: 0 }
  parent = { start: None }

  i = 1
  frontier = [start]

  while frontier:
    next_nodes = []
    for u in frontier:
      for v in adj[u]:
        if v not in level:
          level[v] = i
          parent[v] = u
          next_nodes.append(v)
    frontier = next_nodes
    i += 1

  return level, parent

adj = { 'a' : ['d', 'b'],
        'b' : ['e'],
        'c' : ['e', 'f'],
        'd' : ['b'],
        'e' : ['d'],
        'f' : ['f'] }

start = 'a'

level, parent = bfs(adj, start)


for key, value in level.iteritems():
  print key, " :", value

for key, value in parent.iteritems():
  print key, " :", value
