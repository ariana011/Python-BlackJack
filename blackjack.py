import random
import time

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {str(n): n for n in range(2, 11)}
values.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})

def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[0]
        value += values[rank]
        if rank == 'A':
            aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(hand, owner="Player", reveal_all=True):
    time.sleep(1)
    if owner == "Dealer" and not reveal_all:
        print(f"Dealer's Hand: {hand[0][0]} of {hand[0][1]} and [Hidden]")
        time.sleep(1)
    else:
        print(f"{owner}'s Hand: ", end='')
        time.sleep(1)
        print(', '.join([f"{rank} of {suit}" for rank, suit in hand]))
        time.sleep(1)
        print(f"Total Value: {calculate_hand_value(hand)}\n")

def play_blackjack():
    deck = create_deck()

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("🃏 Welcome to Blackjack! 🃏\n")
    time.sleep(2)
    display_hand(player_hand, "Player")
    time.sleep(2)
    display_hand(dealer_hand, "Dealer", reveal_all=False)

    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    if player_total == 21:
        if dealer_total == 21:
            display_hand(dealer_hand, "Dealer")
            print("Both you and the dealer have Blackjack. It's a tie!")
        else:
            print("🎉 Blackjack! You win!")
        return

    elif dealer_total == 21:
        display_hand(dealer_hand, "Dealer")
        print("Dealer has Blackjack! You lose.")
        return

    while player_total < 21:
        move = input("Do you want to Hit or Stand? (h/s): ").strip().lower()
        if move == 'h':
            card = deck.pop()
            print(f"You drew: {card[0]} of {card[1]}")
            player_hand.append(card)
            display_hand(player_hand, "Player")
            player_total = calculate_hand_value(player_hand)
        elif move == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    if player_total > 21:
        print("💥 You busted! Dealer wins.")
        return

    print("\nDealer's Turn:")
    display_hand(dealer_hand, "Dealer")
    while calculate_hand_value(dealer_hand) < 17:
        card = deck.pop()
        print(f"Dealer draws: {card[0]} of {card[1]}")
        dealer_hand.append(card)
        display_hand(dealer_hand, "Dealer")

    dealer_total = calculate_hand_value(dealer_hand)

    print("\nEnd Result ")
    display_hand(player_hand, "Player")
    display_hand(dealer_hand, "Dealer")

    if dealer_total > 21:
        print("Dealer busted! You win! 😁")
    elif dealer_total > player_total:
        print("Dealer wins.")
    elif dealer_total < player_total:
        print("Congrats You win! 😁")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    while True:
        play_blackjack()
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for playing!🃏")
            break
