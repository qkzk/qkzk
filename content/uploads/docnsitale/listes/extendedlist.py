from list import *

class Extendedlist(List):

    def length (self):
        """
        Return the length of a list
        
        :return: Number of elements in the list

        >>> l = Extendedlist()
        >>> l.length()
        0
        >>> l = Extendedlist(3,l)
        >>> l = Extendedlist(2,l)
        >>> l = Extendedlist(1,l)
        >>> l.length()
        3
        """
        pass
    
    def get(self,i):
        '''
        Get the element at position i (positions start at 0).
        
        :CU: not self.is_empty()

        >>> l = Extendedlist(1, Extendedlist())
        >>> l.get(0)
        1
        >>> l = Extendedlist(4, Extendedlist())
        >>> l = Extendedlist(3,l)
        >>> l = Extendedlist(2,l)
        >>> l = Extendedlist(1,l)
        >>> l.get(3)
        4
        >>> l.get(0)
        1
        '''
        pass
    
            
    def search (self, e):
        """
        Return whether e exists in the list

        :return: True iff e is an element of the list
        
        >>> l = Extendedlist()
        >>> l.search(0)
        False
        >>> l = Extendedlist(3,l)
        >>> l = Extendedlist(2,l)
        >>> l = Extendedlist(1,l)
        >>> l.search(1)
        True
        >>> l.search(3)
        True
        >>> l.search(4)
        False
        """
        pass
    
    def toString (self):
        """
        Return a string representation of the list

        >>> l = Extendedlist()
        >>> l = Extendedlist(3,l)
        >>> l = Extendedlist(2,l)
        >>> l = Extendedlist(1,l)
        >>> l.toString()
        '1 2 3'
        """
        pass

    
    def toPythonList (self):
        """
        Return the Python list corresponding to the list

        :return: A Python list whose length and elements are identical to `self`.

        >>> l = Extendedlist()
        >>> l.toPythonList()
        []
        >>> l = Extendedlist(3,l)
        >>> l = Extendedlist(2,l)
        >>> l = Extendedlist(1,l)
        >>> l.toPythonList()
        [1, 2, 3]
        """
        pass

    
    def sortedInsert(self, x):
        '''
        Insert element x in the list.
        Return a fresh list.

        CU: the list must be sorted according to '<'

        :return: A fresh sorted Extendedlist containing elements of `self`and `x`

        >>> l = Extendedlist()
        >>> l = Extendedlist(4,l)
        >>> l = Extendedlist(2,l)
        >>> l = Extendedlist(1,l)
        >>> l.sortedInsert(3)
        (1.(2.(3.(4.()))))
        >>> l = Extendedlist(4, Extendedlist())
        >>> l.sortedInsert(10)
        (4.(10.()))
        >>> l = Extendedlist(4, Extendedlist())
        >>> l.sortedInsert(1)
        (1.(4.()))
        '''

    def reverse(self):
        '''
        :return: A fresh list containing the same elements as `self`but in reversed order.

        >>> l = Extendedlist()
        >>> l = Extendedlist(3,l)
        >>> l = Extendedlist(2,l)
        >>> l = Extendedlist(1,l)
        >>> l
        (1.(2.(3.())))
        >>> r = l.reverse()
        >>> r
        (3.(2.(1.())))
        '''        
        pass
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
    
