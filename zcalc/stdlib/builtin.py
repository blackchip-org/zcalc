from zcalc.lib import CalcError, op, reduce

@op(aliases=['='])
def apply(z):
    z.stack.append('=')
    z.stack.extend(z.get_stack())
    z.run()

@op(aliases=['c'])
def clear(z):
    z.stack.clear()

@op(aliases=['dn'])
def down(z):
    if len(z.stack) == 0:
        return
    z.stack.insert(0, z.pop())

@op()
def each(z):
    ops = z.get_stack()
    n = len(z.stack)
    for i in range(n):
        z.stack.extend(ops)
        z.run()
        down(z)

@op(aliases=['g'])
def get(z):
    name = z.pop()
    try:
        val = z.vals[name]
        z.stack.append(val)
    except KeyError:
        raise CalcError(f'no such value: {name}')

@op(name='get-stack', aliases=['gs'])
def get_stack(z):
    z.stack.extend(z.get_stack())

@op(aliases=['p'])
def put(z):
    name = z.pop()
    val = z.pop()
    z.vals[name] = val

@op(name='put-stack', aliases=['ps'])
def put_stack(z):
    name = z.pop()
    z.stacks[name] = z.stack
    z.stack = []

@op(aliases=['rev'])
def reverse(z):
    z.stack.reverse()

@op()
def run(z):
    z.run()

@op()
def sort(z):
    z.stack.sort()

@op(aliases=['sw'])
def swap(z):
    a = z.pop()
    b = z.pop()
    z.push(a)
    z.push(b)

@op(aliases=['u'])
def undo(z):
    if len(z.history) <= 1:
        raise CalcError('history empty')
    z.history.pop()
    z.stack = z.history.pop()

@op()
def up(z):
    if len(z.stack) == 0:
        return
    z.stack.append(z.stack.pop(0))

@op()
def use(z):
    z.use(z.pop())

@op()
def vals(z):
    output = []
    names = sorted(list(z.vals.keys()))
    for name in names:
        output.append(f'{name} = {z.vals[name]}')
    z.output = '\n'.join(output)
