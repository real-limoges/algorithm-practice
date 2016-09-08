'''
For i = 1, 2, ... , n:
  Insert A[i] into sorted array, A[0: i-1] by pairwise swaps to the
  correct position.

Original : [5,2,4,6,1,3]
Step 1: [2,5,4,6,1,3]
Step 2: [2,4,5,6,1,3]
Step 3: [2,4,5,6,1,3]
Step 4: [2,4,5,1,6,3]
Step 5: [2,4,1,5,6,3]
...

'''


def insertion_sort(lst):
  '''
  INPUT: Takes a list of a sortable type
  OUTPUT: Returns sorted list.
  
  Standard implementation of insertion sort. 
  
  O(n^2) (each item in lst requires up to n comparisons and swaps) 
  '''
  
  if len(lst) == 0: return lst

  for key in xrange(len(lst)):
      i = key
      while i != 0 and lst[i] < lst[i-1]:
          tmp = lst[i-1]
          lst[i-1] = lst[i]
          lst[i] = tmp
          i -= 1
  return lst

lst = []
print lst
print insertion_sort(lst)
