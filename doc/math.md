# math

Basic mathematical operations.

| Operation             | Alias    | Description
|-----------------------|----------|------------
| [add](#add)           | `a`, `+` | Addition
| [div](#div)           | `d`, `/` | Division
| [frac](#frac)         |          | Converts to fraction
| [int](#int)           |          | Truncates to an integral value
| [mod](#mod)           |          | Remainder of division
| [mul](#mul)           | `m`, `*` | Multiplication
| [prec](#prec)         |          | Gets precision used in decimal operations
| [prec-set](#prec-set) |          | Set precision used in decimal operations
| [round](#round)       | `r`      | Rounds a number
| [sub](#sub)           | `s`, `-` | Subtraction
| [sum](#sum)           |          | Sum all items on the stack

## add

Adds two numbers, `a + b` and puts the `sum` on the stack.

    add ( a:num b:num -- sum:num )

Aliases: `a`, `+`

Example:

| Input   | Stack
|---------|-------------|
| `6`     | `6`
| `2`     | `6 ; 2`
| `a`     | `8`

## div

Divides two numbers, `a / b` and puts the `quotient` on the stack.

    div ( a:num b:num -- quotient:num )

Aliases: `d`, `/`

Example:

| Input   | Stack
|---------|-------------|
| `6`     | `6`
| `2`     | `6 ; 2`
| `d`     | `3`

## frac

Converts a number to a ratio (fraction).

    frac ( num -- rat )

Example:

| Input   | Stack
|---------|-------------|
| `1`     | `1`
| `8`     | `1 ; 8`
| `d`     | `0.125`
| `frac`  | `1/8`

## int

Truncates a number to an integral value.

    int ( num -- int )

Example:

| Input   | Stack
|---------|-------------|
| `7`     | `7`
| `2`     | `7 ; 2`
| `d`     | `3.5`
| `int`   | `3`

## mod

Divides two numbers, `a / b`, and puts the `remainder` on the stack. If `b` is negative, the `remainder` is also negative.

    mod ( a:num b:num -- remainder:int )

Example:

| Input   | Stack
|---------|-------------|
| `7`     | `7`
| `2`     | `7 ; 2`
| `mod`   | `1`

## mul

Multiplies two numbers, `a * b`, and puts the `product` on the stack.

    mul ( a:num b:num -- product:num )

Aliases: `m`, `*`

Example:

| Input   | Stack
|---------|-------------|
| `6`     | `6`
| `2`     | `6 ; 2`
| `m`     | `12`

## prec

Displays the number of significant digits used in decimal operations. Use `prec-set` to change this value. The default value is `16`.

## prec-set

Changes the number of significant digits used in decimal operations.

Example:

| Input         | Stack
|---------------|-------------|
| `2`           | `1`
| `3`           | `1 ; 3`
| `d`           | `0.6666666666666667`
|               |
| `[prec-set 2` |
| `2`           | `1`
| `3`           | `1 ; 3`
| `d`           | `0.67`

## round

Rounds a number to the given number of digits after the decimal point.

    round ( dec int -- num )

Alias: `r`

Example:

| Input         | Stack
|---------------|-------------|
| `2`           | `1`
| `3`           | `1 ; 3`
| `d`           | `0.6666666666666667`
| `[round 2`    | `0.67`

## sub

Subtracts two numbers, `a - b` and puts the `difference` on the stack.

Aliases: `s`, `-`

| Input         | Stack
|---------------|-------------|
| `6`           | `6`
| `2`           | `6 ; 2`
| `s`           | `4`

## sum

Calculates the sum of all numbers on the stack,

    sun ( num... -- num )

Example:

| Input         | Stack
|---------------|-------------|
| `1`           | `1`
| `2`           | `1 ; 2`
| `3`           | `1 ; 2 ; 3`
| `sum`         | `5`
