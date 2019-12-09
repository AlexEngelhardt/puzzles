from itertools import permutations
from computer import Computer

debug = False

filename = 'test-input' if debug else 'input'

with open(filename) as f:
    memory = list(map(int, f.read().split(',')))


def try_permutation(permutation, debug):
    # 4: "phase setting", i.e. permutation of 0,1,2,3,4
    # 0: output of previous amp. First input is 0
    ampA = Computer(memory.copy(), inputs=[permutation[0], 0],
                    debug=debug)
    outputA = ampA.run()

    ampB = Computer(memory.copy(), inputs=[permutation[1], outputA],
                    debug=debug)
    outputB = ampB.run()

    ampC = Computer(memory.copy(), inputs=[permutation[2], outputB],
                    debug=debug)
    outputC = ampC.run()

    ampD = Computer(memory.copy(), inputs=[permutation[3], outputC],
                    debug=debug)
    outputD = ampD.run()

    ampE = Computer(memory.copy(), inputs=[permutation[4], outputD],
                    debug=debug)
    outputE = ampE.run()

    return(outputE)


perms = permutations([0, 1, 2, 3, 4])

max_output = 0

for perm in perms:
    res = try_permutation(perm, debug=False)
    max_output = max(max_output, res)
    print(perm, ':', res)

print(max_output)
