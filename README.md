# Computer-Architecture-Labs
computer Architecture labs for my university's student, dept/IT, Level-2 

# Lab 5
1. **Addition Simulation (`de97b0b9-...`)**:
   - Simulates an assembly-like processor that executes `Add` instructions from a memory list.
   - Registers are updated by adding values from two source registers and storing the result in a third.

2. **Load Simulation (`f194ab1b-...`)**:
   - Simulates a processor executing `Load` instructions.
   - Loads a constant value into a register.

3. **Subtraction Simulation (`aacc8466-...`)**:
   - Executes `Sub` instructions from memory.
   - Performs subtraction between two registers and stores the result in a third.


# Lab 6
1. **RAM Simulation (`92754836-...`)**:
   - Defines a `RAM` class that simulates simple memory operations:
     - `stor(index, data)`: Stores data at a specified memory index.
     - `read(index)`: Reads data from a given index.
     - `show(index)`: Displays data at a given index.
   - Demonstrates storing and reading the value `'Ali'` at index 8.

2. **CPU Register Simulation (`88a2c0af-...`)**:
   - Defines a `CPU` class simulating register operations:
     - `load(reg, value)`: Loads a value into a register.
     - `inc(reg)`: Increments the value of a register by 1.
     - `dec(reg)`: Decrements the value of a register by 1.
     - `display(reg)`: Displays the current value of a register.
   - Demonstrates loading and displaying a value in register `R2`.
