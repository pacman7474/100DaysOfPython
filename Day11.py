import random

deck = {
    "A": [11,1],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}

def draw_card(hand):
    new_card = random.choice(list(deck))
    hand = hand.append(new_card)
    print(f"A {new_card} was drawn.")
    return hand

def check_hand(hand):
    total = 0
    for card in hand:
        if card != "A":
            total += deck[card]
        else:
            if total + deck["A"][0] > 21:
                total += deck["A"][1]
            else:
                total += deck["A"][0]
    return total

play_game = True
continue_playing = input("Would you like to play a game of Blackjack? (Y/N): ").upper()
if continue_playing == "Y":
    play_game = True
else:
    play_game = False

while play_game:
    game_over = False
    dealer_hand = [random.choice(list(deck)), random.choice(list(deck))]
    player_hand = [random.choice(list(deck)), random.choice(list(deck))]
    player_total = 0
    dealer_total = 0
    if check_hand(dealer_hand) == 21:
        if check_hand(player_hand) == 21:
            print("Both players get Blackjack and push.")
        else:
            print("Dealer gets Blackjack and Wins.")
    elif check_hand(player_hand) == 21:
        print("Player wins with Blackjack.")
    else:
        print(f"Players Hand: {player_hand[0]}, {player_hand[1]}")
        print(f"Dealers Hand: {dealer_hand[0]}, ??")
        new_card = True
        player_draw_card = input("Would you like a card? (Y/N): ").upper()
        while player_draw_card == "Y":
            draw_card(player_hand)
            player_total = check_hand(player_hand);
            print(f"Your current total is: {check_hand(player_hand)}")
            if player_total > 21:
                player_draw_card = "N"
                game_over = True
            else:
                player_draw_card = input("Would you like a card? (Y/N): ").upper()
        while check_hand(dealer_hand) < 18 and game_over == False:
            print("Dealer draws a card.")
            draw_card(dealer_hand)
            dealer_total = check_hand(dealer_hand)
            if dealer_total > 21:
                game_over = True
        player_total = check_hand(player_hand)
        dealer_total = check_hand(dealer_hand)
        game_over = True
        print(f"Your hand: {player_hand}")
        print(f"Your total is: {player_total}")
        print(f"Dealer's hand: {dealer_hand}")
        print(f"The dealer's total is: {dealer_total}")
        if game_over == True:
            if dealer_total > 21:
                print("Dealer busted. You Win!")
            elif player_total > 21:
                print("You busted. Dealer wins.")
            elif player_total > dealer_total:
                print("Congratulations! You win!")
            elif dealer_total > player_total:
                print("Sorry you lose. Dealers wins.")
            elif dealer_total == player_total:
                print("You push.")
    continue_playing = input("Would you like to play again? (Y/N): ").upper()
    if continue_playing == "N":
        play_game = False
    else:
        play_game = True