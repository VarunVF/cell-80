import sys

def run(code):
    lines = code.splitlines()
    tape = [0] * 80
    pc = 0
    jmp = 0
    
    def tape_reset():
        nonlocal tape
        tape = [0] * 80
    
    while pc < len(lines):
        line = lines[pc]
        if len(line) != 80:
            # Tape reset: Line did not have 80 columns
            tape_reset()
        
        jumped = False
        for i in range(0, 80):
            if jumped:
                break
            
            if line[i] == "#":
                pass
            elif line[i] == "+":
                tape[i] += 1
            elif line[i] == "-":
                tape[i] -= 1
            elif line[i] == ".":
                print(chr(tape[i]), end="")
            elif line[i] == ":":
                print(tape[i], end="")
            elif line[i] == ",":
                tape[i] = int(input())
            elif line[i] == "!":
                if i == 79:
                    jmp = pc
                else:
                    # Tape reset: '!' found outside last column
                    tape_reset()
            elif line[i] == "?":
                if tape[i] != 0:
                    pc = jmp
                    jumped = True
            else:
                # Tape reset: Unknown operation
                tape_reset()
        
        if not jumped:
            pc += 1

def main():
    args = sys.argv
    if len(args) == 2:
        with open(sys.argv[1]) as f:
            run(f.read())
    elif len(args) < 2:
        print("No script file provided")
        sys.exit(-1)
    else:
        print("Too many arguments")
        sys.exit(-1)

if __name__ == "__main__":
    main()
