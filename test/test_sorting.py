from nose.tools import assert_equals

from sorting.insertion_sort import insertion_sort

def test_empty_insertion_sort():
  lst = []

  assert_equals(insertion_sort(lst), [])

def test_normal_insertion_sort():
  lst = [5,2,4,6,1,3]
  correct = [1,2,3,4,5,6]

  assert_equals(insertion_sort(lst), correct) 

