# bit

Bitwise operations.

| Operation                   | Alias       | Description
|-----------------------------|-------------|------------
| [and](#and)                 | `&`         | Bitwise and
| [bin](#bin)                 |             | Convert to a binary integer
| [hex](#hex)                 |             | Convert to a hexadecimal integer
| [oct](#oct)                 |             | Convert to an octal integer
| [or](#or)                   | `` \| ``    | Bitwise or
| [shift-left](#shift-left)   | `<<`, `shl` | Shift bits left
| [shift-right](#shift-right) | `>>`, `shr` | Shift bits right
| [xor](#xor)                 | `^`         | Bitwise exclusive-or

## and

Bitwise and between two integers.

    and ( int int -- int )

Alias: `&`

Example:

| Input       | Stack
|-------------|-------------|
| `0x88`      | `0x88`
| `0xf0`      | `0x88 ; 0xf0`
| `and ; hex` | `0x80`

## bin

Convert an integer to binary.

    and ( int -- int )

Example:

| Input       | Stack
|-------------|-------------|
| `0x0f`      | `0x0f`
| `bin`       | `0b1111`

## dec

Convert in integer \to decimal.

    dec ( int -- int )

Example:

| Input       | Stack
|-------------|-------------|
| `0x0f`      | `0x0f`
| `dec`       | `15`

## hex

Convert an integer to hexadecimal.

Example:

| Input       | Stack
|-------------|-------------|
| `127`       | `127`
| `hex`       | `0x7f`

## oct

Convert an integer to octal.

    oct ( int -- int )

Example:

| Input       | Stack
|-------------|-------------|
| `420`       | `420`
| `oct`       | `0o644`

## or

Bitwise or between two integers.

    and ( int int -- int )

Alias: `|`

Example:

| Input       | Stack
|-------------|-------------|
| `0x88`      | `0x88`
| `0xf0`      | `0x88 ; 0xf0`
| `or ; hex`  | `0xf8`

## shift-left

Shift the integer `a` to the left by `b` bits. This is the same as multiplying by `2 * b`.

    shift-left ( a:int b:int -- int )

Aliases: `<<`, `shl`

| Input        | Stack
|--------------|-------------|
| `32`         | `32`
| `1`          | `32 ; 1`
| `shift-left` | `64`

## shift-right

Shift the integer `a` to the right by `b` bits. The same as dividing by `2 * b`.

    shift-right ( a:int b:int -- int )

Aliases: `>>`, `shr`

| Input         | Stack
|---------------|-------------|
| `64`          | `64`
| `1`           | `64 ; 1`
| `shift-right` | `32`

## xor

Bitwise exclusive-or between two integers.

    xor ( int int -- int )

Alias: `^`

Example:

| Input       | Stack
|-------------|-------------|
| `0x0f`      | `0x0f`
| `0xff`      | `0x0f ; 0xff`
| `xor ; hex` | `0xf0`
