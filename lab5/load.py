memory = [
    "Load R1, 5",
    "Load D1, 3",
    "Load V1, 9",
    
]

PC = 0

Register = {
    "R1": 100,
    "D1": 110,
    "V1": 130,
}

# fetch the line of code(instraction) from the memory that stor code
def fetch():
    global PC
    instraction = memory[PC]
    PC += 1
    return instraction


# Decoding the instraction that came from fetch step(phase) to it's basic parts
def decoding(instraction):
    parts = instraction.split()
    opcode = parts[0]
    operands = parts[1].split(',')
    return opcode, operands


# Execute the decoded instraction 
def exceution(opcode, operands):
    if opcode == 'load':
        reg, val = operands
        Register[reg] = int(val)
        print(f"{reg} = {Register[reg]}")

# Loop through all instractions in memory  
while True:
    # check if the PC:(program counter) reachs to last instraction or not yet
    # this mean if pc value is greater than the number of instraction
    if PC < len(memory):
        instraction = fetch()
        opcode, operands = decoding(instraction)
        exceution(opcode, operands)
    else:
        print("Program End Execution")
        break