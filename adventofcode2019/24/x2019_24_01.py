import numpy as np


class Field:
    def __init__(self, data):
        field = []
        for d in data:
            field.append([1 if x == '#' else 0 for x in d])

        self.field = np.array(field)

    def biodiversity(self):
        return (self.field.flatten() * (np.ones(25)*2 ** np.arange(0, 25))).sum().astype(int)

    def evolve(self):
        new_grid = self.field.copy()
        for i in range(5):
            for j in range(5):
                neighbors_alive = 0
                if i > 0:
                    neighbors_alive += self.field[i - 1, j]
                if j > 0:
                    neighbors_alive += self.field[i, j - 1]
                if i < 4:
                    neighbors_alive += self.field[i + 1, j]
                if j < 4:
                    neighbors_alive += self.field[i, j + 1]

                if self.field[i, j] and neighbors_alive != 1:
                    new_grid[i, j] = 0
                elif not self.field[i, j] and neighbors_alive in [1, 2]:
                    new_grid[i, j] = 1
        self.field = new_grid.astype(int)


def main():
    with open('input') as file:
        field = file.read().splitlines()
    print(field)

    f = Field(field)
    print(f.field)

    f.evolve()
    print(f.field)

    seen_fields = set()

    while f.biodiversity() not in seen_fields:
        seen_fields.add(f.biodiversity())
        f.evolve()

    print(f.biodiversity())


if __name__ == '__main__':
    main()
