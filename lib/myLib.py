author = 'mnoumanshahzad'


def _map(func_, list_):
    """
    Applies the given function to each item of the list
    :param func_:
    :param list_:
    :return: A new list of transformed items
    """
    return [func_(item) for item in list_]


def _reduce(func_, list_):
    """
    Applies to the list of items to reduce the result to a single item
    :param func_:
    :param list_:
    :return: A single, aggregated item
    """
    if len(list_) == 1:
        return list_[0]
    else:
        head = list_.pop(0)
        aggr = reduce(func_, list_)
        return func_(head, aggr)

def _filter(func_, list_):
    """
    FIlters the given list according to the predicate function provided
    :param func_: Predicate function that returns a boolean value
    :param list_:
    :return: List of filtered items that are true for the predicate
    """
    return [item for item in list_ if func_(item)]

def _foldl(func_, list_):
    """
    Consumes the list of elements with left associativity
    :param func_:
    :param list_:
    :return: A single aggregated value
    """
    acc = list_.pop(0)
    for item in range(len(list_)):
        acc = func_(acc, list_.pop(0))
    return acc

def _foldr(func_, list_):
    """
    Consumes the list of elements with right associativity
    :param func_:
    :param list_:
    :return: A single aggregated value
    """
    acc = list_.pop()
    for item in range(len(list_)):
        acc = func_(acc, list_.pop())
    return acc

def _foreach(func_, list_):
    """
    Iterates over a list of elements and applies the given
    functions on each element of the list
    :param func_:
    :param list_:
    :return:
    """
    for index, item in enumerate(list_):
        func_(item)

def _zip(flist, slist):
    """
    _zip takes in two lists as arguments and 
    pair up each element of the list at the 
    respective index
    :param flist: 
    :param slist: 
    :return: A list of 2-tuples
    """
    result = list()
    for i in range(min(len(flist), len(slist))):
        result.append((flist[i], slist[i]))
    return result
