from nose.tools import assert_equals

from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge

def test_insertion_sort_empty():
  '''
  Tests insertion sort if given an empty list
  '''

  lst = []

  assert_equals(insertion_sort(lst), [])

def test_insertion_sort_normal():
  '''
  Tests insertion sort given a normal list
  '''

  lst = [5,2,4,6,1,3]
  correct = [1,2,3,4,5,6]

  assert_equals(insertion_sort(lst), correct) 

def test_merge_sort_merge_both_empty():
  '''
  Tests merge_sort's merge function when given two empty lists
  '''

  l, r = [], []
  correct = []

  assert_equals(merge(l, r), correct)

def test_merge_sort_merge_one_empty():
  '''
  Tests merge_sort's merge function when given left or right empty
  '''

  l_empty, r_empty = [], []
  l = [1,3,5]
  r = [2,4,6]


  assert_equals(merge(l_empty, r), [2,4,6])
  assert_equals(merge(l, r_empty), [1,3,5])

def test_merge_sort_merge_normal():
  '''

  '''

  l, r = [1,4,7], [2,3,6]
  correct = [1,2,3,4,6,7]

  assert_equals(merge(l,r), correct)

