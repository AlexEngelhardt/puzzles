from itertools import permutations
from computer import Computer, ExitOpcode

debug = False

filename = 'test-input2' if debug else 'input'

with open(filename) as f:
    memory = list(map(int, f.read().split(',')))


def try_permutation(permutation, debug):
    # 4: "phase setting", i.e. permutation of 0,1,2,3,4
    # 0: output of previous amp. First input is 0
    ampA = Computer(memory.copy(), inputs=[permutation[0]], debug=debug)
    ampA.inputs.append(0)

    ampB = Computer(memory.copy(), inputs=[permutation[1]], debug=debug)
    ampC = Computer(memory.copy(), inputs=[permutation[2]], debug=debug)
    ampD = Computer(memory.copy(), inputs=[permutation[3]], debug=debug)
    ampE = Computer(memory.copy(), inputs=[permutation[4]], debug=debug)

    while True:

        try:
            outputA = ampA.run()
            ampB.inputs.append(outputA)
            outputB = ampB.run()
            ampC.inputs.append(outputB)
            outputC = ampC.run()
            ampD.inputs.append(outputC)
            outputD = ampD.run()
            ampE.inputs.append(outputD)
            outputE = ampE.run()
            ampA.inputs.append(outputE)  # feedback *loop*
        except ExitOpcode:
            break

    return(outputE)


perms = permutations([5, 6, 7, 8, 9])

max_output = 0

for perm in perms:
    res = try_permutation(perm, debug=False)
    max_output = max(max_output, res)
    print(perm, ':', res)

print(max_output)
