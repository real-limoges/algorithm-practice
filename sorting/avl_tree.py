'''
Balanced Binary Search Trees

Insert n items in O(n*log(n)). We're guaranteed that O(h) ~ O(log(n)) due
to the self balancing nature of the tree.

Inorder Traversal in O(n)

Abstract Data Type - Specifications of what you want (Priority Queue, etc..)

Data Structure - Actual implementation (Heap, AVL, etc...)
'''

class Node:
  '''
  Node Class
  '''

  def __init__(self, value):
    self.value = value
    self.height = 0
    self.l_child = None
    self.r_child = None


  def set_height(self):
    '''
    Sets the height for the tree
    '''
    
    if self.l_child is None and self.r_child is None:
      self.height = 0
    elif self.l_child is not None and self.r_child is None:
      self.height = self.l_child.height + 1
    elif self.l_child is None and self.r_child is not None:
      self.height = self.r_child.height + 1
    else:
      self.height = max(self.l_child.height, self.r_child.height) + 1
   

  def set_l_child(self, node):
    '''
    Sets the l_child
    '''

    self.l_child = node


  def set_r_child(self, node):
    '''
    Sets the r_child
    '''

    self.r_child = node



class AVL_Tree:
  '''
  AVL_Tree

  Requires the heights of left and right child of every node to differ
  by at most +- 1. Maintenance in log(n) time.
  '''

  def __init__(self, root=None):
    self.root = root

  def set_root(self, root):
    '''
    Sets the root of the tree
    '''

    self.root = root


  def left_rotate(self):
    '''
    Rotates the AVL_Tree to the left
    '''

  def right_rotate(self):
    '''
    Rotates the AVL_Tree to the right
    '''


def insert_node(root, node):
  '''
  Inserts a node
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


lst = [41, 20, 65, 11, 29, 26, 60, 26, 23]


tree = AVL_Tree()

for item in lst:
  if tree.root is None:
    tree.set_root( Node(item) )
  else:
    insert_node(tree.root, Node(item))


print tree.root.value
