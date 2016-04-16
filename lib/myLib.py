author = 'mnoumanshahzad'


def _map(func_, list_):
  """
  Applies the provided function on the specified list
  :return: List of transformed items
  """
  return [func_(item) for item in list_]


def _reduce(func_, list_):
    result = None
    for i in range(len(list_) - 1):
        if i == 0:
            temp = list_[i]
        else:
            temp = result
        result = func_(temp, list_[i + 1])
    return result


