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


deck = Deck(10)
deck.stack
deck.deal_with_increment(7)
deck.deal_into_new_stack()
deck.deal_into_new_stack()
deck.stack

deck = Deck(10)
deck.deal_with_increment(7)
deck.deal_with_increment(9)
deck.cut(-2)
deck.stack
