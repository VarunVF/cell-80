# cell-80

A small esolang.

## Syntax

The machine is 80-cell memory tape, with a jump register.
The tape is initally set to all 0.
Each line must have exactly 80 columns, every character in a line can modify the cell at that column.
Execution flows line by line, and all operations on cells of a line occur together.

If any rules are broken, the tape will reset to all 0 without any warning or error.
Good luck finding the bug.

Operators:
- `#` : no-op
- `+` : increment cell
- `-` : decrement cell
- `,` : input value from the user into cell, expects an integer
- `.` : print cell as ascii
- `:` : print cell as number
- `!` : set jump register to current line, only allowed on last column
- `?` : jump if cell is not zero (execution continues at line stored in jump register)

The trailing newline characters (`CR`, `LF`) are allowed.
Other characters are not allowed.

Example programs:
- `add-six.c80`: Takes an integer as user input, adds 6, shifts the result to another cell, then prints the result.
- `hello-world.c80`: Hello world program, using loops.
