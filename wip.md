# wip

Maryland sales tax rounds up. Get this to work:

    `tax [round-rule up] 1.06 m [round-rule half-even]

Then:

| Input            | Stack
|------------------|-------------|
| `1.01`           | `1.01`
| `=tax`           | `1.08`

Working on an example but maybe this could be done in a better way.

Add a debugging mode to see stack operations.

## Example

Here is a quick example of using this RPN calculator. Let's say that we are
deciding on getting either a standard room or a suite on our next vacation
and we want to compute the difference in price between the two. The prices are:

- $280/night for standard
- $315/night for suite
- $19.95/night service fee
- 5% sales tax
- 2.5% lodging tax

We will be staying at the hotel for six nights. The service fee is going to
be the same for both rooms so let's compute that first and store it as a
macro:

| Input            | Stack
|------------------|-------------|
| `19.95`          | `19.95`
| `6`              | `19.95 ; 6`
| `m`              | `119.7`
| `` `fee ``       |

Calculate the expensive room first:

| Input            | Stack
|------------------|-------------|
| `315`            | `315`
| `6`              | `315 ; 6`
| `m`              | `1890`

Both taxes are are based on the pre-tax value. Let's duplicate the sub-total
and compute the sales tax:

| Input            | Stack
|------------------|-------------|
| `cp`             | `1890 ; 1890`
| `0.05`           | `1890 ; 1890 ; 0.05`
| `m`              | `1890 ; 94.5`

Swap the values on the stack and do the same to compute the lodging tax:

| Input            | Stack
|------------------|-------------|
| `sw`             | `94.5 ; 1890`
| `cp`             | `94.5 ; 1890 ; 1890`
| `0.025`          | `94.5 ; 1890 ; 0.25`
| `m`              | `94.5 ; 1890 ; 47.25`

We now have the base price and both taxes. Now add the fee and add them all
together for the final total.

| Input            | Stack
|------------------|-------------|
| `=fee`           | `94.5 ; 1890 ; 47.25 ; 119.7`
| `a`              | `94.5 ; 1890 ; 166.95`
| `a`
