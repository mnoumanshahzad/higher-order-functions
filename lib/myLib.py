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


