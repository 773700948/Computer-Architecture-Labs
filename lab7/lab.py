class CPU:
    def __init__(self):
        self.program = []
        self.register = {'R1':0,'R2':0,'R3':0,'R4':0, 'R5':0}
        self.pc = 0
        self.memory = [0] * 100


    # load program to memory
    def load_program(self, program):
        self.program = program

    # feach the instraction
        # to do code
    def feach(self):
        print('Stage 1 : Feach')
        if self.pc < len(self.program):
            instraction  = self.program[self.pc]
            print(f'Feached instraction = [{instraction}]')
            return instraction
        else:
            print(f'No instraction found...')
            return None
        

    # decode the instraction
        # to do code
    def decoding(self, instraction):
        print('Stage-2 : Decoding')
        parts = instraction.split()
        opcode = parts[0]
        operands = parts[1].split(',')

        print(f'Decoded instraction: opcode = {opcode}, operands = {operands}')
        return opcode, operands


    # execute the instraction
    
    def execute(self, opcode, operands):
        print('Stage-3 : Execute')
        result = None
        if opcode == 'ADD':
            result = self.register[operands[0]] + self.register[operands[1]]
        elif opcode == 'SUB':
            result = self.register[operands[0]] - self.register[operands[1]]
        elif opcode == 'MULT':
            result = self.register[operands[0]] * self.register[operands[1]]
        elif opcode == 'DIV':
            result = self.register[operands[0]] / self.register[operands[1]]
        elif opcode == 'MOV':
            result = int(operands[1])
        
        return result


    # access memory
        # to store or load 
    def access_memory(self, opcode, operands, result):

        print('Stage-4 : access memory')
        if opcode == 'STORE':

            index = int(operands[1])
            self.memory[index] = self.register[operands[0]]


            print(f' Data in {operands[0]} stored successfully into memory[{index}]')

        elif opcode == 'LOAD':
            index = int(operands[1])

            result = self.memory[index]
            print(f'Loaded {result} from memory[{index}]')

        return result


    # write back in memory
        # write values from the registers to the memory
    def write_back(self, opcode, operands, result):
        print('Stage-5 : write the result of operation')
        if opcode in ["ADD", "SUB", "MOV", "LOAD"]:
            self.register[operands[0]] = result
            print(f'New value of {operands[0]} = {result}')
        
    def show_state(self):
        print('=' * 40)
        print(f'PC = {self.pc}')
        print(f'Registers = {self.register}')
        print(f'Memory = {self.memory[:11]}')
        print('=' * 40)
    # # run method
    #     # go through the instraction life cycle

    def run(self, program):
        # load the program to be execute
        self.load_program(program=program)

        # go through the program list each time take: instraction 
        while True:
            # instraction life cycle
            if self.pc < len(self.program):
                # input('Press Enter 🚓 to execute the nex instraction 💻.....')
                inst = self.feach()
                opcode , operands = self.decoding(inst)
                result = self.execute(opcode, operands)
                result = self.access_memory(opcode, operands, result)
                self.write_back(opcode, operands, result)
                self.show_state()
                self.pc += 1

            else:
                break


program = [
    # operation 1
    "MOV R1,10",
    "MOV R2,5",
    "ADD R1,R2",
    "STORE R1,0",
    # operation 2
    "LOAD R3,0",
    "MOV R4,12",
    "ADD R3,R4",
    "STORE R3,1",


    "LOAD R5,0",
    "MOV R6,1",
    "Sub R5,R6"
    "Store R5,2"
    # "PRINT R2",
    # "PRINT 1",
]

cpu = CPU()

cpu.run(program)

    
