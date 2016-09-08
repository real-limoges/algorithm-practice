'''
Divide and Conquer sorting algorithm.

Split A -> L, R. Sorts L, R -> L', R'. Merges and returns the concatenation

It uses a lot more space than insertion sort (which is in-place) but
has a n*log(n) efficiency rather than n^2.
'''

def merge(l, r):
  '''
  INPUTS: l, r are ascending sorted arrays.
  OUTPUT: One merged array

  Takes two lists (can be empty) and merges them in ascending order.   
  '''
  merged = []
  
  while len(l) > 0 or len(r) > 0:
    if len(l) == 0:
      merged.append( r.pop(0) )
    elif len(r) == 0:
      merged.append( l.pop(0) )
    elif l[0] > r[0]:
      merged.append( r.pop(0) )
    else:
      merged.append( l.pop(0) )
 
  return merged

def merge_sort(lst):
  '''
  INPUT: list to be sorted
  OUTPUT: Merged

  If the list has 0 elements (empty list) it returns the list.
  If the list is 1 element, it returns the list. 

  Else it splits the list into a left and right half and recursively
  calls merge_sort until it is one item. Then it returns the singleton
  which is recursively merged.
  '''
  if len(lst) <= 1:
    return lst

  mid = len(lst)//2
  left = merge_sort(lst[:mid])
  right = merge_sort(lst[mid:])

  return merge(left, right)
