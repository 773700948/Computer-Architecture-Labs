# Register operation
'''
- INC: add 1 to reg value
- DEC: sub 1 of reg value
- Display: show reg contant
- Load: assign value to re
'''
class CPU:
    register = {
        'R1' : 0,
        'R2' : 0,
        'R3' : 0,
        'R4' : 0,
        }
    keys = list(register.keys())
    # load data to reg
    def load(self, reg: int, value):
        self.register[reg] = value
        print(f'value {value} has been loaded successfully ot register {reg} ')
    # increment reg value by 1
    def inc(self, reg):
        self.register[reg] += 1
        print(f'{reg} is incremented succeesfully')
    # decrement reg value with 1
    def dec(self, reg):
        self.register[reg] -= 1
        print(f'{reg} is decremented succeesfully')
    # display reg value
    def display(self, reg):
        print(f'{reg} = {self.register[reg]}')

cpu = CPU()
keys = cpu.keys
cpu.load(reg=keys[1],value=50)
cpu.display(keys[1])