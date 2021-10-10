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
| [undo](#undo)       | `u`   | Undo the last action
| [use](#use)         |       | Import operations from module

## apply

Invoke the `=` macro.

    clear ( any... -- any... )

Alias: `=`

Example:

| Input            | Stack
|------------------|-------------|
| `` `= 2 *``      |
| `3`              | `3`
| `=`              | `6`

## clear

Clears the stack.

    clear ( any... -- )

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

    copy ( any -- any any )

Alias: `cp`

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `cp`    | `1 ; 1`

## down

Rotates the stack by moving all items down. The top of the stack moves to the bottom of the stack.

    down ( any... -- any... )

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

    each ( any... -- any... )

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

    reverse ( any... -- any... )

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

    sort ( any... -- any... )

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

    swap ( any any -- any any )

Alias: `sw`

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `2`     | `1 ; 2`
| `3`     | `1 ; 2 ; 3`
| `sw`    | `1 ; 3 ; 2`

## undo

Undo the last action. Up to 25 actions are stored in history.

    undo ( any... -- any... )

Alias: `u`

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `2`     | `1 ; 2`
| `a`     | `3`
| `u`     | `1 ; 2`

## up

Rotates the stack by moving all items up. The bottom of the stack moves to the top of the stack.

    up ( any... -- any... )

Alias: `up`

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `2`     | `1 ; 2`
| `3`     | `1 ; 2 ; 3`
| `up`    | `3 ; 1 ; 2`

## use

Import operations from the specified module.

    use ( name -- )

Example:

| Input       | Stack
|-------------|-------------|
| `[use unit` |
| `0`         | `0`
| `C->F`      | `32`
