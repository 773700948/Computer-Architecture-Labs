'''
# RAM operation
- stor data
- read data: get data from memory
- show data
- clear: rest memory

'''

class RAM:
    data_memory = [0] * 10
    # stor data in memory
    def stor(self, index , data):
        if 0 < index < len(self.data_memory):
            self.data_memory[index] = data
            print(f'{data} is stored successfully in index: {index}')
        else:
            print(f'{index} is out of range')
    # read data from memory
    def read(self, index):
        if 0 < index < len(self.data_memory):
            return self.data_memory[index]
        else:
            print(f'{index} is out of range')
            return None
    # show data in sepsific address
    def show(self, index):
        if 0 < index < len(self.data_memory):
            print(f'Address {index} = {self.data_memory[index]} ')
        else:
            print(f'{index} is out of range')
    # to show spesific data
    def show(self, index):
        if 0 < index < len(self.data_memory):
            print(f'Data in index[{index}] = {self.read(index)}')
        else:
            print(f'{index} is out of range')

ram = RAM()
ram.stor(8, 'Ali')
ram.read(8)