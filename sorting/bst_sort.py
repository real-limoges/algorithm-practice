'''
Binary Search Tree (BST)

Pointers to parent(x), left(x), right(x)

Invariant: For all nodes x, if y is in the left subtree of x, 
key(y) <= key(x) If y is in the right subtree, key(y) >= key(x)


'''

# Class Declarations

class Node:
  '''
  Node:
    This is a data point in the binary search tree.

    Attributes:
      Value - This is the key for the Node
      L_Child - The left child. Always less than the parent
      R_Child - The right child. Always greater than or equal to the parent

  '''

  def __init__(self, value):
    self.value = value
    self.l_child = None
    self.r_child = None
  
  def add_l_child(self, l_child):
    '''
    Sets the l_child for the Node
    '''

    self.l_child = l_child

  def add_r_child(self, r_child):
    '''
    Sets the r_child for the Node
    '''

    self.r_child = r_child

  def print_val(self):
    '''
    Prints the value of the Node to the terminal
    '''

    print self.value


class Tree:
  '''
  Tree:
    This is the structure holding the BST.

    Attributes:
      Root - This is a pointer to the root of the tree
  '''

def __init__(self, root=None):
    self.root = root

  def has_root(self):
    '''
    Returns if the Tree has a root. Default setup of Tree is None
    '''
    
    return self.root is None


  def set_root(self, root):
    '''
    Sets the root of the Tree with given passed Node 
    '''
    
    self.root = root


  def count_nodes(self):
    '''
    INPUTS: None
    OUTPUTS: Returns the count of the nodes in the tree

    If there is no root, returns 0
    Else it calls _count_nodes to recursively count the nodes
    '''

    if self.root is not None:
      return self._count_nodes(self.root)
    return 0


  def _count_nodes(self, node):
    '''
    INPUT: Node
    OUTPUT: Count of nodes

    Recursively calls _count_nodes to find the number of nodes in the tree
    If the node is None, it returns 0
    If the node is a leaf, it returns 1
    Else it returns 1 + sum(left) + sum(right)
    '''
    
    if node is None:
      return 0
    elif node.l_child is None and node.r_child is None:
      return 1
    else:
      return (1 + self._count_nodes(node.l_child) +
                  self._count_nodes(node.r_child) )


# Function Declarations


def insert_node(root, node):
  '''
  INPUTS: Root Node (Tree must already have one node), Node to insert
  OUTPUTS: None

  Inserts a node into a BST.
  '''

  if root.value > node.value:
    if root.l_child is None:
      root.l_child = node
    else:
      insert_node(root.l_child, node)
  else:
    if root.r_child is None:
      root.r_child = node
    else:
      insert_node(root.r_child, node)

def inorder(root, lst):
  '''
  INPUTS: Current Root node, list to be modified
  OUTPUTS: None (side effects only)

  Does an in order traversal of the BST. Recursively calls.
  Appends values (in order) to a list. Done with side effects to 
  avoid returning at the end.
  '''
  
  if root:
    if root.l_child is None and root.r_child is None:
      lst.append(root.value)
    else:
      inorder(root.l_child, lst)
      lst.append(root.value)
      inorder(root.r_child, lst)


def bst_sort(lst):
  '''
  INPUT: Unsorted List
  OUTPUT: Sorted List
 
  Takes in an unordered list, creates a tree, and then creates a new
  sorted array by reading the values in-order.
  '''
  
  s_lst = []

  myTree = Tree()
  for item in lst:
    if myTree.root is None:
      myTree.set_root( Node(item) )
    else:
      insert_node(myTree.root, Node(item))

  inorder(myTree.root, s_lst)

  return s_lst
