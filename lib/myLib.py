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