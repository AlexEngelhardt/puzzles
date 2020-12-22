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


class Game:
    def __init__(self, deck1, deck2, debug=False):
        self.debug = debug
        self.deck1 = deque(deck1)
        self.deck2 = deque(deck2)
        self.rounds_played = 0
        self.game_over = False
        self.winner = None
        self.configurations_seen = set()

    def play_round(self):
        self.rounds_played += 1
        if self.debug:
            print()
            print(f'Starting round {self.rounds_played}:')
            print(f'Player 1: {self.deck1}')
            print(f'Player 2: {self.deck2}')

        if (tuple(self.deck1), tuple(self.deck2)) in self.configurations_seen:
            # Then player 1 wins
            self.game_over = True
            self.winner = 1
            return
        else:
            self.configurations_seen.add((tuple(self.deck1), tuple(self.deck2)))

        if not (self.deck1 and self.deck2):
            self.game_over = True
            self.winner = 1 if not self.deck2 else 2
            return

        card1 = self.deck1.popleft()
        card2 = self.deck2.popleft()

        if len(self.deck1) >= card1 and len(self.deck2) >= card2:
            if self.debug:
                print('Starting subgame')
            new_deck1 = list(self.deck1)
            if card1 < len(new_deck1):
                new_deck1 = new_deck1[:card1]
            new_deck2 = list(self.deck2)
            if card2 < len(new_deck2):
                new_deck2 = new_deck2[:card2]
            subgame = Game(new_deck1, new_deck2, debug=self.debug)
            winner = subgame.play()
            if winner == 1:
                self.deck1.append(card1)
                self.deck1.append(card2)
            elif winner == 2:
                self.deck2.append(card2)
                self.deck2.append(card1)
        else:
            if card1 > card2:
                self.deck1.append(card1)
                self.deck1.append(card2)
            elif card2 > card1:
                self.deck2.append(card2)
                self.deck2.append(card1)

    def play(self):
        while not self.game_over:
            self.play_round()
        return self.winner

    def compute_score(self):
        stack = self.deck1 if self.deck1 else self.deck2
        multiplier = list(reversed(range(1, len(stack)+1)))
        score = sum([stack[i] * multiplier[i] for i in range(len(stack))])
        return score


G = Game(deck1, deck2, debug=debug)
winner = G.play()
print(G.compute_score())
