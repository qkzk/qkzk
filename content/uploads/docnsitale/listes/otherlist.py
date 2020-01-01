class ListError(Exception):
    """
    Exception used by methods

    * ``__init__``
    * ``head``
    * ``tail``
    
    of class :class:`List`.
    """
    def __init__(self, msg):
        self.message = msg
    
class List(object):

    def __init__ (self, *args):
        '''
        Builds a new list.
        As explained in the `Readme.md` a list can either be:
        * empty;
        * built from an element an a list.

        Either we don't have any arguments, or two arguments.

        :param *args: The arguments to the function. Either no argument is provided
        or two are provided (the second one being a list).
        :CU: len(args) == 0 or (len(args) == 2 and args[1] is a List)
        '''
        if len(args) == 0:
            # No parameter: builds an empty list
            self.__cell = None
        elif len(args) == 2:
            # Two parameters: an element and a list
            if isinstance(args[1],List):
                self.__cell = { "head" : args[0], "tail": args[1]}
            else:
                raise ListError("Second argument must be a List")                
        else:
            raise ListError("Bad arguments number")

    def head (self):
        '''
        Return the head of the list

        :return: first element of the list

        >>> l=List(1, List())
        >>> l.head()
        1
        >>> l = List(2, List(1, List()))
        >>> l.head()
        2
        >>> l = List()
        >>> l.head()
        Traceback (most recent call last):
        ...
        ListError
        '''
        if not self.is_empty():
            return self.__cell['head']
        raise ListError("empty list has no head")
    
    def tail (self):
        '''
        Return the tail of the list

        :return: the list without its first element

        >>> l=List(1, List())
        >>> l.tail()
        ()
        >>> l = List(2, List(1, List()))
        >>> l.tail()
        (1.())
        >>> l = List()
        >>> l.head()
        Traceback (most recent call last):
        ...
        ListError
        '''
        if not self.is_empty():
            return self.__cell['tail']
        raise ListError("empty list has no tail")


    def is_empty (self):
        '''
        Returns whether the list is empty

        :return: True iff the list doesn't have any element

        >>> List().is_empty()
        True
        >>> List(1, List()).is_empty()
        False
        '''
        return self.__cell == None


    def set_tail (self, l):
        '''
        Replaces the tail of the list by l. 
        Raises ListError if applied on an empty list.
        Raises ListError if l is not a List.

        >>> l1 = List(1,List(2,List()))
        >>> l2 = List(3,List(4,List()))
        >>> l1.set_tail(l2)
        >>> l1
        (1.(3.(4.())))        
        >>> l = List()
        >>> l.set_tail(l1)
        Traceback (most recent call last):
        ...
        ListError        
        '''
        assert(isinstance(l,List))
        if self.is_empty():
            raise ListError("can't change tail of an empty list")
        else:
            self.__cell['tail'] = l

    def set_head (self, e):
        '''
        Replaces the head of the list by e. 
        Raises ListError if applied on an empty list.

        >>> l = List()
        >>> l.set_head(3)
        Traceback (most recent call last):
        ...
        ListError        
        >>> l = List(1,List())
        >>> l.set_head(3)
        >>> l
        (3.())
        >>> l = List(1,List(2,List()))
        >>> l.set_head(3)
        >>> l
        (3.(2.()))
        ''' 
        if self.is_empty():
            raise ListError("can't change head of an empty list")
        else:
            self.__cell['head'] = e
    
    def __repr__ (self):
        """
        Returns the dot notation of a list

        >>> l = List(1,(List(2,(List(3,List())))))
        >>> repr(l)
        '(1.(2.(3.())))'
        """
        if self.is_empty():
            return '()'
        else:
            return '('+repr(self.head())+'.'+repr(self.tail())+')'
    

    
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
