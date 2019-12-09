
# Stolen from:
# https://emkc.org/s/JJk0Dn


class Intcode:

    def __init__(self, debug=False):
       self.program = None
       self.cursor = 0


       self.log = lambda *args, **kwargs: print(*args, flush=True, **kwargs) if debug else lambda *args, **kwargs: None

       self.ops = {
               1: self._ADD,
               2: self._MUL,
               3: self._IN,
               4: self._OUT,
               5: self._JUMP_IF_TRUE,
               6: self._JUMP_IF_FALSE,
               7: self._LESS_THAN,
               8: self._EQUALS,
               99: self._EXIT
        }

    
    def run(self, program):
        self.program = program
        
        while True:
            self._execute(self.program[self.cursor])

        return self.program

    def _execute(self, command):
        self.log(f"EXECUTE({command})")

        code, mode = self._parse(command)

        self.log(f"OPCODE {code}, mode {mode}")

        self.ops[code](mode)


    def _parse(self, command):

        self.log(f"PARSE({command})")


        command = str(command)

        opcode = int(command[-2:])
        mode = command[:-2]
        if not mode:
            mode = 0
        mode = int(mode)

        
        self.log(f"parsed for opcode {opcode} and mode {mode}")

        return opcode, mode

    def _read(self, cell, mode):

        self.log(f"READ({cell}, mode={mode})")


        if mode == 0:
            val = self.program[cell]
            self.log(f"read {val}")
            return val

        elif mode == 1:
            self.log(f"read {cell}")
            return cell


    def _ADD(self, mode):

        self.log(f"ADD(mode={mode})")


        v1 = self.program[self._read(self.cursor+1, mode%10)]
        v2 = self.program[self._read(self.cursor+2, (mode//10)%10)]

        to_stock = self._read(self.cursor+3, (mode//100)%10) 
        self.program[to_stock] = v1 + v2

        self.cursor += 4

        
    def _MUL(self, mode):

        self.log(f"MUL({mode})")

        v1 = self.program[self._read(self.cursor+1, mode%10)]
        v2 = self.program[self._read(self.cursor+2, (mode//10)%10)]
 
        to_stock = self._read(self.cursor+3, (mode//100)%10)
        self.program[to_stock] = v1 * v2

        self.cursor += 4


    def _IN(self, mode):
        self.log(f"IN({mode})")


        inp = int(input("Enter a value : "))

        to_stock = self._read(self.cursor+1, mode%10)

        self.log(f"stored {inp} to position {to_stock}")
        self.program[to_stock] = inp

        self.cursor += 2

    
    def _JUMP_IF_TRUE(self, mode):
        self.log(f"JUMP_IF_TRUE({mode})")
        
        param1 = self.program[self._read(self.cursor+1, mode%10)]
        param2 = self.program[self._read(self.cursor+2, (mode//10)%10)]

        if param1:
            self.cursor = param2

        else:
            self.cursor += 3

     
    def _JUMP_IF_FALSE(self, mode):
        self.log(f"JUMP_IF_FALSE({mode})")   


        param1 = self.program[self._read(self.cursor+1, mode%10)]
        param2 = self.program[self._read(self.cursor+2, (mode//10)%10)]

        if not param1:
            self.cursor = param2

        else:
            self.cursor += 3


    def _LESS_THAN(self, mode):
        self.log(f"LESS_THAN({mode})")
        param1 = self.program[self._read(self.cursor+1, mode%10)]
        param2 = self.program[self._read(self.cursor+2, (mode//10)%10)]
        param3 = self._read(self.cursor+3, (mode//100)%10)


        if param1 < param2:
            self.program[param3] = 1
        else:
            self.program[param3] = 0

        self.cursor += 4

    def _EQUALS(self, mode):
        self.log(f"EQUALS({mode})")
        param1 = self.program[self._read(self.cursor+1, mode%10)]
        param2 = self.program[self._read(self.cursor+2, (mode//10)%10)]
        param3 = self._read(self.cursor+3, (mode//100)%10)


        if param1 == param2:
            self.log("is equal!")
            self.program[param3] = 1
        else:
            self.log("not equal.")
            self.program[param3] = 0

        self.cursor += 4


    def _OUT(self, mode):
        self.log(f"OUT({mode})")

        to_read = self.program[self._read(self.cursor+1, mode%10)]

        self.log("output is ", end='')

        print(to_read)
        
        self.cursor += 2

    def _EXIT(self, mode):
        raise SystemExit("Done")
        



if __name__ == "__main__":
    
    with open("input.txt") as f:
        program = list(map(int, f.read().split(',')))

    
    #program = [3,9,8,9,10,9,4,9,99,-1,8]
    computer = Intcode(debug=False)

    computer.run(program)
