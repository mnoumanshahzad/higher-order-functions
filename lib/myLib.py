author = 'mnoumanshahzad'

def _map(func_, list_):
  """
  Applies the provided function on the specified list
  :return: List of transformed items
  """
  return [func_(item) for item in list_]

