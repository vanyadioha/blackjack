import random
from constant import cards


def deal_card(deck, is_initial):
    if is_initial:
        for _ in range(2):
            deal = random.choice(cards)
            deck.append(deal)
    else:
        deal = random.choice(cards)
        deck.append(deal)
