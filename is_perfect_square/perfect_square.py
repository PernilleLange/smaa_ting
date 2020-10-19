from decimal import *
import cmath

def is_perfect_square(num, *, complex=False):
    if complex is True:
        try:
            prelim = str(cmath.sqrt(num))
            return '.' not in prelim
        except:
            raise TypeError
    else:
        if num < 0:
            return False
        else:
            getcontext().prec = 700
            return Decimal(num).sqrt() % 1 == 0



