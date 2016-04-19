author = 'mnoumanshahzad'

from lib.myLib import _map, _reduce, _filter

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]
natural = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

str_data_1 = ['HI', 'HAHA', 'BOO', 'NOO', 'YES']

def _sqr(number):
  return number * number

def _cube(number):
    return number * number * number

def _mul(number_1, number_2):
    return number_1 * number_2

def _concat(str_1, str_2):
    return str_1 + " " + str_2

def _map_sqr_odd():
  return _map(_sqr, odd)

def _map_sqr_even():
    return _map(_sqr, even)

def _reduce_mul_odd():
    return _reduce(_mul, odd)

def _reduce_mul_even():
    return _reduce(_mul, even)

def _reduce_concat():
    return _reduce(_concat, str_data_1)

def test_map():
    print 'Testing "_map"'
    print '_map(_sqr, {odd_list}) --> {result} '.format(odd_list=odd, result=_map_sqr_odd())
    print '_map(_sqr, {even_list}) --> {result} '.format(even_list=even, result=_map_sqr_even())
    print

def test_reduce():
    print 'Testing "_reduce"'
    print '_reduce(_mul, {odd_list}) --> {result}'.format(odd_list=odd, result=_reduce_mul_odd())
    print '_reduce(_mul, {even_list}) --> {result}'.format(even_list=even, result=_reduce_mul_even())
    print '_reduce(_concat, {str_list}) --> {result}'.format(str_list=str_data_1, result=_reduce_concat())
    print

def main():
    test_map()
    test_reduce()

if __name__ == '__main__':
    main()