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
    self.l_child = None
    self.r_child = None


class AVL_Tree:
  '''
  AVL_Tree

  Requires the heights of left and right child of every node to differ
  by at most +- 1. Maintenance in log(n) time.
  '''

  def __init__(self):
    self.root = None
    self.height = -1
    self.balance = 0


  def insert_node(self, val):
    '''
    Inserts a node into the AVL_Tree
    '''
    
    node = Node(val)
    
    if self.root is None:
      self.root = node
      self.root.l_child = AVL_Tree()
      self.root.r_child = AVL_Tree()
    
    elif node.value < self.root.value:
      self.root.l_child.insert_node(val)
    
    else:
      self.root.r_child.insert_node(val)

    self.rebalance_tree()


  def rebalance_tree(self):
    '''
    Rebalances the AVL_Tree. Called after every insert/delete.
    '''
    
    self.update_height(recursive = False)
    self.update_balance(False)

    # If the balance is over 1 or under -1, then it breaks the
    # AVL_Tree invariant
    while self.balance < -1 or self.balance > 1:
      if self.balance > 1:
        if self.root.l_child.balance < 0:
          self.root.l_child.left_rotate()
          self.update_height()
          self.update_balance()
  
        self.right_rotate()
        self.update_height()
        self.update_balance()
      
      elif self.balance < -1:
        if self.root.r_child.balance > 0:
          self.root.r_child.right_rotate()
          self.update_height()
          self.update_balance()
        self.left_rotate() 
        self.update_height()
        self.update_balance()
  
  
  def update_height(self, recursive=True):
    '''
    Updates the height for each node.
    '''

    if self.root is not None:
      if recursive is True:
        if self.root.l_child is not None:
          self.root.l_child.update_height()
        if self.root.r_child is not None:
          self.root.r_child.update_height()
      self.height = 1 + max(self.root.l_child.height,
                            self.root.r_child.height)
     
    else:
      self.height = -1

  
  def update_balance(self, recursive=True):
    '''
    Updates the balance for each node
    '''

    if self.root is not None:
      if recursive == True:
        if self.root.l_child is not None:
          self.root.l_child.update_balance()
        if self.root.r_child is not None:
          self.root.r_child.update_balance()
      
      self.balance = self.root.l_child.height - self.root.r_child.height
    
    else:
      self.balance = 0


  def right_rotate(self):
    '''
    Rotates the AVL_Tree to the right
    '''

    new_root = self.root.l_child.root
    new_left_subtree = new_root.r_child.root
    old_root = self.root

    self.root = new_root
    old_root.l_child.root = new_left_subtree
    new_root.r_child.root = old_root


  def left_rotate(self):
    '''
    Rotates the AVL_Tree to the left
    '''

    new_root = self.root.r_child.root
    new_right_subtree = new_root.l_child.root
    old_root = self.root

    self.root = new_root
    old_root.r_child.root = new_right_subtree
    new_root.l_child.root = old_root


  def avl_sort(self):
    '''
    Returns an inorder traversal of the AVL_Tree. Since the AVL_Tree
    is a BST, an inorder traversal takes O(n) to print once constructed.

    INPUT: None
    OUTPUT: List (In-Order Traversal)
    '''
    
    result = []

    if self.root is None:
      return result

    result.extend(self.root.l_child.avl_sort())
    result.append(self.root.value)
    result.extend(self.root.r_child.avl_sort())

    return result

lst = [41, 20, 65, 11, 29, 26, 60, 26, 23]


tree = AVL_Tree()

for item in lst:
  tree.insert_node(item)

print tree.avl_sort()
