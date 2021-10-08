# builtin

## apply (=)

Invoke the `=` macro.

Example:

| Input            | Stack
|------------------|-------------|
| `` `= 2 *``      |
| `3`              | `3`
| `=`              | `6`

## clear (c)

Clears the stack.

    clear ( ... -- )

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `2`     | `1 ; 2`
| `3`     | `1 ; 2 ; 3`
| `c`     |

## copy (cp)

Creates a copy of the top item on the stack.

    copy ( a -- a a )

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `cp`    | `1 ; 1`

## down (dn)

Rotates the stack by moving all items down. The top of the stack moves to the bottom of the stack.

    down ( a b c -- c a b )

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `2`     | `1 ; 2`
| `3`     | `1 ; 2 ; 3`
| `dn`    | `3 ; 1 ; 2`

## each

Apply the specified macro, rotate the stack, and repeat *n* times where *n* is the number of items on the stack. Useful for applying a macro to each item of the stack if the macro consumes one item as input and emits one item.

    each ( a1 b1 c1 -- a2 b2 c2 )

Example:

| Input            | Stack
|------------------|-------------|
| `` `double 2 *`` |
| `1`              | `1`
| `2`              | `1 ; 2`
| `3`              | `1 ; 2 ; 3`
| `[each double`   | `2 ; 4 ; 6`

## reverse (rev)

Reverses the items on the stack.

    reverse ( a b c -- c b a )

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `2`     | `1 ; 2`
| `3`     | `1 ; 2 ; 3`
| `rev`   | `3 ; 2 ; 1`

## sort

Sorts the items on the stack.

    sort ( b d a c -- a b c d )

Example:

| Input   | Stack
|---------|-------------|
| `2`     | `2`
| `4`     | `2 ; 4`
| `1`     | `2 ; 4 ; 1`
| `3`     | `2 ; 4 ; 1 ; 3`
| `sort`  | `1 ; 2 ; 3 ; 4`

## swap (sw)

Swap the first two items on the stack.

    swap ( a b c -- a c b )

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `2`     | `1 ; 2`
| `3`     | `1 ; 2 ; 3`
| `sw`    | `1 ; 3 ; 2`

## use

Import the specified module.

    import ( a -- )

Example:

| Input       | Stack
|-------------|-------------|
| `[use unit` |
| `0`         | `0`
| `C->F`      | `32`

