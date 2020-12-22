from collections import deque

debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    contents = f.read().strip()
p1, p2 = contents.split('\n\n')


def parse(p):
    p = p.split('\n')[1:]
    p = list(map(int, p))
    return p


deck1 = parse(p1)
deck2 = parse(p2)

print(deck1)
print(deck2)


class Game:
    def __init__(self, deck1, deck2, debug=False):
        self.deck1 = deque(deck1)
        self.deck2 = deque(deck2)
        self.rounds_played = 0
        self.game_over = False

    def play_round(self):
        if not (self.deck1 and self.deck2):
            self.game_over = True
            return
        card1 = self.deck1.popleft()
        card2 = self.deck2.popleft()

        if card1 > card2:
            self.deck1.append(card1)
            self.deck1.append(card2)
        elif card2 > card1:
            self.deck2.append(card2)
            self.deck2.append(card1)
        else:
            raise
        self.rounds_played += 1
        if debug:
            print()
            print(f'After {self.rounds_played} rounds:')
            print(f'Player 1: {self.deck1}')
            print(f'Player 2: {self.deck2}')

    def play(self):
        while not self.game_over:
            self.play_round()
        print('finish :3')

    def compute_score(self):
        stack = self.deck1 if self.deck1 else self.deck2
        multiplier = list(reversed(range(1, len(stack)+1)))
        score = sum([stack[i] * multiplier[i] for i in range(len(stack))])
        return score


G = Game(deck1, deck2, debug=debug)
G.play()
print(G.compute_score())
