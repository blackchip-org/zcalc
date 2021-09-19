from zcalc.lib import CalcError, op, reduce

@op()
def all(z):
    op_stack = z.get_stack()
    reduce(op_stack)

@op(aliases=['c'])
def clear(z):
    z.stack.clear()

@op()
def each(z):
    name = z.pop()
    try:
        op_stack = z.stacks[name]
    except KeyError:
        raise CalcError(f'no such stack: {name}')
    n = len(z.stack)
    for i in range(n):
        z.stack.extend(op_stack)
        z.run()
        rotate(z)

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
    name = z.pop()
    try:
        stack = z.stacks[name]
        for item in stack:
            z.stack.append(item)
    except KeyError:
        raise CalcError(f'no such stack: {name}')

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

@op(aliases=['rot'])
def rotate(z):
    if len(z.stack) == 0:
        return
    z.stack.insert(0, z.pop())

@op(aliases=['='])
def run(z):
    z.run()

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
