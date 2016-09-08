from nose.tools import assert_equals

from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge, merge_sort
from sorting.heap_sort import build_max_heap, heap_sort

#TODO
'''
Test heap_sort's max_heapify
Test all of bst_sort
'''

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
  Tests merge_sort's merge function with non-empty lists
  '''

  l, r = [1,4,7], [2,3,6]
  correct = [1,2,3,4,6,7]

  assert_equals(merge(l,r), correct)


def test_merge_sort_merge_sort_empty():
  '''
  Tests merge_sort's merge_sort function with an empty list
  '''

  lst = []

  assert_equals(merge_sort(lst), [])


def test_merge_sort_merge_sort_normal():
  '''
  Tests merge_sort's merge_sort function with an unordered list
  '''

  lst = [5,2,4,6,1,3]
  correct = [1,2,3,4,5,6]

  assert_equals(merge_sort(lst), correct)


def test_heap_sort_build_max_heap_empty():
  '''
  Tests heap_sort's build_max_heap function with empty list
  '''

  lst = []
  correct = []

  assert_equals(build_max_heap(lst), correct)


def test_heap_sort_build_max_heap_normal():
  '''
  Tests heap_sort's build_max_heap function with unordered list
  '''

  lst = [5,2,4,6,1,3]
  correct = [6,5,4,2,1,3]

  assert_equals(build_max_heap(lst), correct)


def test_heap_sort_heap_sort_empty():
  '''
  Tests heap_sort's heap_sort function with empty list
  '''

  lst = []
  correct = []

  assert_equals(heap_sort(lst), correct)


def test_heap_sort_heap_sort_normal():
  '''
  Tests heap_sort's heap_sort function with unordered list
  '''

  lst = [5,2,4,6,1,3]
  correct = [6,5,4,3,2,1]

  assert_equals(heap_sort(lst), correct)
