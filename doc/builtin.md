# builtin

Operations that are always available in zcalc. These are mostly stack
manipulation operations, shortcuts, or administrative tasks.

| Operation           | Alias | Description
|---------------------|-------|------------
| [apply](#apply)     | `=`   | Invoke the `=` macro
| [clear](#clear)     | `c`   | Clears the stack
| [copy](#copy)       | `cp`  | Creates a copy of the top item on the stack
| [down](#down)       | `dn`  | Rotates the stack by moving all items down
| [each](#each)       |       | Applies an operation to each item on the stack
| [reverse](#reverse) | `rev` | Reverses the items on the stack
| [sort](#sort)       |       | Sorts the items on the stack
| [swap](#swap)       | `sw`  | Swap first two items on the stack
| [use](#use)         |       | Import operations from module

## apply

Invoke the `=` macro.

Alias: `=`

Example:

| Input            | Stack
|------------------|-------------|
| `` `= 2 *``      |
| `3`              | `3`
| `=`              | `6`

## clear

Clears the stack.

    clear ( ... -- )

Alias: `cp`

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `2`     | `1 ; 2`
| `3`     | `1 ; 2 ; 3`
| `c`     |

## copy

Creates a copy of the top item on the stack.

    copy ( a -- a a )

Alias: `cp`

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `cp`    | `1 ; 1`

## down

Rotates the stack by moving all items down. The top of the stack moves to the bottom of the stack.

    down ( a b c -- c a b )

Alias: `dn`

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

## reverse

Reverses the items on the stack.

    reverse ( a b c -- c b a )

Alias: `rev`

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

## swap

Swap the first two items on the stack.

    swap ( a b c -- a c b )

Alias: `sw`

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `2`     | `1 ; 2`
| `3`     | `1 ; 2 ; 3`
| `sw`    | `1 ; 3 ; 2`

## use

Import operations from the specified module.

    use ( a -- )

Example:

| Input       | Stack
|-------------|-------------|
| `[use unit` |
| `0`         | `0`
| `C->F`      | `32`

