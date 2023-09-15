from functions import deal_card
from art import blackjack

print(blackjack)

player = []
dealer = []
keep_drawing_player = True
keep_drawing_dealer = True

deal_card(player, True)
deal_card(dealer, True)

player_sum = sum(player)
dealer_sum = sum(dealer)

print(f"Player: {player}")
print(f"Dealer: {[dealer[0]]}")

if player_sum == 21 and dealer_sum == 21:
    print("Draw!")
elif player_sum == 21:
    print("Player Won with a Blackjack!")
elif dealer_sum == 21:
    print("Dealer won with a Blackjack!")
else:
    while keep_drawing_player:
        player_sum = sum(player)
        if player_sum > 21 & 11 in player:
            player.remove(11)
            player.append(1)
            player_sum = sum(player_sum)
        if player_sum > 21:
            print("You Lose")
            keep_drawing_player = False
        if keep_drawing_player:
            draw_card = input("Do you want to draw another card? 'Y' or 'N': ")
            if draw_card.upper() == "Y":
                deal_card(player, False)
            else:
                keep_drawing_player = False
        print(player)

    while keep_drawing_dealer:
        dealer_sum = sum(dealer)
        if dealer_sum < 17:
            deal_card(dealer, False)
        else:
            keep_drawing_dealer = False
    print(dealer)

    if dealer_sum > 21 and player_sum > 21:
        print("You Draw")
    elif dealer_sum > 21:
        print("You Win")
    elif player_sum > 21:
        print("You Lose")
    elif player_sum < dealer_sum:
        print("You Lose")
    elif player_sum > dealer_sum:
        print("You Win")
    else:
        print("It was a draw")
