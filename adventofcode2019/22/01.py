import os
os.chdir('/home/alexx/github/puzzles/adventofcode2019/22')


class Deck():
    def __init__(self, n_cards):
        self.stack = list(range(n_cards))
        self.n_cards = n_cards

    def deal_into_new_stack(self):
        self.stack.reverse()

    def cut(self, n):
        if n < 0:
            # cutting 4 from bottom is the same as cutting n-4 from top
            n = self.n_cards + n  # plus because n is negative :)
        self.stack = self.stack[n:] + self.stack[:n]

    def deal_with_increment(self, n):
        new_stack = self.stack.copy()
        for i in range(self.n_cards):
            new_stack[(i*n) % self.n_cards] = self.stack[i]
        self.stack = new_stack


deck = Deck(10007)

with open('input') as f:
    for line in f:
        line = line.strip()
        if line == 'deal into new stack':
            deck.deal_into_new_stack()
        elif line.startswith('cut'):
            deck.cut(int(line.split(' ')[-1]))
        elif line.startswith('deal with increment'):
            deck.deal_with_increment(int(line.split(' ')[-1]))

deck.stack.index(2019)
