# zcalc

[![Build Status](https://app.travis-ci.com/blackchip-org/zcalc.svg?branch=main)](https://app.travis-ci.com/blackchip-org/zcalc)

A fun RPN calculator.

Work in progress.

To install and run from PyPI:

```bash
pip3 install zcalc
zcalc
```

## Usage

When running `zcalc` a prompt is presented. When a line is entered and the
prompt, it first checked to see if it is the name of an operation. If so, that
operation is performed. Otherwise, the line is placed on the stack.

An example of adding two numbers:

| Input            | Stack
|------------------|-------------|
| `1`              | `1`
| `2`              | `1 ; 2`
| `a`              | `3`

With the first line, `1`, it does not match an operation so its value is
placed on the stack. The next line is a `2` and is also placed on the stack.
When `a` is entered, that matches the addition operation. The first two
items are popped from the stack, the result is added, and the result is
placed back on the stack.

When examples are presented in this input/stack table format, each row
shows the state of the *stack* after *input* is entered at the prompt.
Stack items are separated by semicolons and the top element on the stack
is at the right.

Operations may have name aliases. The addition operation has a standard long form (`add`), a traditional operator form (`+`) and a short form that is easy
to type without the use of the shift key (`a`).

The basic math operations are as follows:

| Operation        | Description
|------------------|-----------------|
| `add`, `+`, `a`  | addition
| `sub`, `-`, `s`  | subtraction
| `mul`, `*`, `m`  | multiplication
| `div`, `/`, `d`  | division

More basic math operations can be found in the [math](doc/math.md) module documentation.

### Stack Operations

Pop the top item from the stack by entering a blank line:

| Input            | Stack
|------------------|-------------|
| `1`              | `1`
| `2`              | `1 ; 2`
|                  | `1`

Clear the entire stack with `clear` or `c`:

| Input            | Stack
|------------------|-------------|
| `1`              | `1`
| `2`              | `1 ; 2`
| `c`              |


## Development Setup

In general:

```bash
pip3 install -e .
zcalc
```

Setup python 3.7 environment on macOS:

```bash
brew install python@3.7
/usr/local/opt/python@3.7/bin/python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -e .
```

Setup environment on Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .
```

Running tests:

```bash
pip install pytest
python -m unittest
```

## License

MIT
