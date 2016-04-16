author = 'mnoumanshahzad'

from lib.myLib import _map

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]
natural = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def _sqr(number):
  return number * number

def cube(number):
    return number * number * number

def _map_sqr_odd():
  return _map(_sqr, odd)

def _map_sqr_even():
    return _map(_sqr, even)

def test_map():
    print '_map(_sqr, {odd_list}) --> {result} '.format(odd_list=odd, result=_map_sqr_odd())
    print '_map(_sqr, {even_list}) --> {result} '.format(even_list=even, result=_map_sqr_even())


def main():
    test_map()

if __name__ == '__main__':
    main()