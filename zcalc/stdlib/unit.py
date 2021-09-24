from decimal import Decimal
from zcalc.lib import op, reduce

@op(name='C->F')
def c_to_f(z):
    z.do([
        z.pop(),
        1.8,
        '*',
        32,
        '+',
    ])


