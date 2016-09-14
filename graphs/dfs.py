def dfs_visit( adj, start ):
  '''
  INPUTS:
  OUTPUTS: None (Side Effects Only)

  Recursively searches for everything reachable from a single node.
  It places the parent of a given node, is placed in the parent dictionary
  '''
  
  for v in adj[start]:
    if v not in parent:
      parent[v] = start
      dfs_visit( adj, v )

def dfs(adj):
  '''
  INPUTS: List of Vertices (V); Dictionary of Lists (adj)
  OUTPUTS: None (Side Effects Only)

  Iterates through each vertex in V and recursively visits each node
  reachable from it. If the vertex has been seen, it skips the vertex.

  This runs in O(|V| + |E|) time.
  '''
  for s, _ in adj.iteritems():
    if s not in parent:
      parent[s] = None
      dfs_visit(adj, s)

 
adj = { 'a' : ['d', 'b'],
        'b' : ['e'],
        'c' : ['e', 'f'],
        'd' : ['b'],
        'e' : ['d'],
        'f' : ['f'] }
parent = {}

dfs(adj)

for key,value in parent.iteritems():
  print key, " :", value
