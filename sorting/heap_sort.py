'''
Heap Data Structure:
  Array visualized as a (nearly) complete binary tree

[1,2,3,4,5,6,7,8,9,10] <- 10 elements so not complete
[16,14,10,8,7,9,3,2,4,1] <- Keys

Root of tree is the first element in array.
Parent of i = i/2
Left child of i = 2*i
Right child of i = 2*i + 1

Max Heap property: Key of node >= keys of node's children
'''

def max_heapify(lst, index):
  '''
  INPUT: List becoming a heap; index
  OUTPUT: None (inplace)

  Corrects a single violation of the max heap property in a subtree's
  root. If one of the children is larger, then it swaps with the parent.
  If both left and right are larger, right is swapped due to implementation

  O(log(n)) since it only goes the depth of the subtree. Worst case starts
  at the top.
  '''

  left_c = index * 2 + 1
  right_c = index * 2 + 2
  max_index = index

  if left_c < len(lst) and lst[left_c] > lst[max_index]:
    max_index = left_c
  
  if right_c < len(lst) and lst[right_c] > lst[max_index]:
    max_index = right_c

  if max_index != index:
    lst[index], lst[max_index] = lst[max_index], lst[index]
    max_heapify(lst, max_index)


def build_max_heap(lst):
  '''
  INPUT: Unordered list
  OUTPUT: Max-heap list.

  Converts a max heap from an unordered array.

  Each operation is log(n). Each is done n times.
  Overall O(n*log(n)) efficiency. Done in-place.
  '''

  for index in xrange(len(lst)//2, -1, -1):
    max_heapify(lst, index)

  return lst

def heap_sort(lst):
  s_lst = []

  build_max_heap(lst)

  while len(lst) != 0:
    s_lst.append( lst.pop(0) )
    build_max_heap(lst)

  return s_lst

