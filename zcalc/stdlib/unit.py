from decimal import Decimal
from zcalc.lib import op, reduce

@op(name='C->F')
def c_to_f(z):
    z.op1(lambda n: (n * Decimal(1.8)) + 32, z.pop_number)


