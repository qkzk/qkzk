from myqueue import Queue

def parse(doc):
    """
    :param doc: (str) a document to be parsed
    :return: (Queue) a queue containing tag (without attributes)
    :CU: None
    :Example:

    >>> q = parse("<!DOCTYPE html><html><div class='titre'>du contenu ignoré</div></html>")
    >>> q.is_empty()
    False
    >>> q.dequeue() == "<html>"
    True
    >>> q.dequeue() == "<div>"
    True
    >>> q.dequeue() == "</div>"
    True
    >>> q.dequeue() == "</html>"
    True
    >>> q.is_empty()
    True
    >>> # Other example
    >>> q = parse("<html><div><p <a")
    >>> q.dequeue() == "<html>"
    True
    >>> q.dequeue() == "<div>"
    True
    >>> q.is_empty()
    True
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
