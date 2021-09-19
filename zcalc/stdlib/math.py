import operator
from zcalc.lib import op, reduce

@op(aliases=['+', 'a'])
def add(z):
    z.op2(operator.add, z.pop_number)

@op(aliases=['/', 'd'])
def div(z):
    z.op2(operator.truediv, z.pop_number)

@op()
def frac(z):
    def fn(d):
        (num, denom) = d.as_integer_ratio()
        return f'{num}/{denom}'
    z.op1(fn, z.pop_decimal)

@op(name='int')
def int_(z):
    z.op1(int, z.pop_number)

@op(aliases=['%'])
def mod(z):
    z.op2(operator.mod, z.pop_number)

@op(aliases=['*', 'm'])
def mul(z):
    z.op2(operator.mul, z.pop_number)

@op()
def neg(z):
    z.op1(operator.neg, z.pop_number)

@op()
def norm(z):
    z.op1(lambda d: d.normalize(), z.pop_decimal)

@op(aliases=['-', 's'])
def sub(z):
    z.op2(operator.sub, z.pop_number)

@op()
def sum(z):
    reduce(z, ['add'])

