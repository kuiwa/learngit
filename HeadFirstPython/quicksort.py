# -*- coding: utf-8 -*-
# file: quicksort.py
#
class quick_sort(object):
    def _partition(self, alist, p, r):
        i = p-1
        x = alist[r]
        for j in range(p, r):
            if alist[j]<=x:
                i += 1
                alist[i], alist[j] = alist[j], alist[i]
        alist[i+1], alist[r] = alist[r], alist[i+1]
        return i+1
 
    def _quicksort(self, alist, p, r):
        if p<r:
            q = self._partition(alist, p, r)
            self._quicksort(alist, p, q-1)
            self._quicksort(alist, q+1, r)
 
    def __call__(self, sort_list):
        self._quicksort(sort_list, 0, len(sort_list)-1)
        return sort_list
lis = [ 7, 10, 11, 30, 20, 21, 22, 20, 2, 3, 4, 1 ]
root = quick_sort(lis)
print root
