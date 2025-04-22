memory = [
    "Add R1,R2,R3",
    "Add D1,D2,D3",
    "Add V1,V2,V3",
    "Add G1,G2,G3",
]

PC = 0

Register = {
    "R1": 100,
    'R2':150,
    'R3':0,
    "D1": 110,
    'D2':155,
    'D3':0,
    "V1": 130,
    'V2':152,
    'V3':0,
    "G1": 210,
    'G2':155,
    'G3':0,
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
    if opcode == 'Add':
        r1, r2, r3= operands
        Register[r3] = Register[r1] + Register[r2]
        print(f'{Register[r1]} + {Register[r2]} = {Register[r3]}')
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