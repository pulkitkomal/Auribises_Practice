from random import shuffle

# define the card ranks, and suits
ranks = [_ for _ in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['SPADE', 'HEART ', 'DIAMOND', 'CLUB']

def get_deck():
    """Return a new deck of cards."""

    return [[rank, suit] for rank in ranks for suit in suits]

# get a deck of cards, and randomly shuffle it
deck = get_deck()
shuffle(deck)

player_in = True

# issue the player and dealer their first two cards
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]