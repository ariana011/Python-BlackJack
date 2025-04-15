import random
import time

suits = ['Hearts ♥️', 'Dia️monds ♦️', 'Clubs ♣️', 'Spades ♠️']
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
    for rank, _ in hand:
        value += values[rank]
        if rank == 'A':
            aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(hand, owner="Player", reveal_all=True):
    if owner == "Dealer" and not reveal_all:
        print(f"Dealer's Hand: {hand[0][0]} of {hand[0][1]} and [Hidden]")
        time.sleep(1)
    else:
        print(f"{owner}'s Hand: " + ', '.join([f"{rank} of {suit}" for rank, suit in hand]))
        time.sleep(1)
        print(f"Total Value: {calculate_hand_value(hand)}\n")
        time.sleep(1)

def offer_insurance(dealer_hand, player_chips):
    if dealer_hand[0][0] == 'A':
        choice = input("Dealer shows an Ace. Do you want to take insurance? (y/n): ").lower()
        time.sleep(1)
        if choice == 'y':
            bet = min(10, player_chips // 2)
            print(f"Insurance bet placed: {bet} chips")
            time.sleep(1)
            return bet
    return 0

def check_blackjack(hand):
    return calculate_hand_value(hand) == 21 and len(hand) == 2

def play_blackjack():
    chips = 100
    while chips > 0:
        print(f"\nYou have {chips} chips.")
        time.sleep(1)
        try:
            bet = int(input("Place your bet: "))
            time.sleep(1)
            if bet > chips or bet <= 0:
                print("Invalid bet.")
                time.sleep(1)
                continue
        except ValueError:
            print("Enter a valid number.")
            time.sleep(1)
            continue

        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        insurance_bet = offer_insurance(dealer_hand, chips)

        display_hand(player_hand, "Player")
        display_hand(dealer_hand, "Dealer", reveal_all=False)

        if check_blackjack(player_hand):
            if check_blackjack(dealer_hand):
                display_hand(dealer_hand, "Dealer")
                print("Both have Blackjack. It's a tie! 🤝")
                time.sleep(1)
            else:
                print(" Blackjack! You win 1.5x your bet! 😁")
                time.sleep(1)
                chips += int(1.5 * bet)
            continue

        if check_blackjack(dealer_hand):
            display_hand(dealer_hand, "Dealer")
            print("Dealer has Blackjack!🃏")
            time.sleep(1)
            if insurance_bet:
                chips += 2 * insurance_bet
                print(f"Insurance paid out: {2 * insurance_bet} chips")
                time.sleep(1)
            chips -= bet
            continue

        action = input("Choose: (h)it, (s)tand, (d)ouble down, (u)surrender: ").lower()
        time.sleep(1)
        if action == 'u':
            print("You surrendered. Half your bet is returned.")
            time.sleep(1)
            chips -= bet // 2
            continue
        if action == 'd':
            if bet * 2 <= chips:
                bet *= 2
                card = deck.pop()
                print(f"You drew: {card[0]} of {card[1]}")
                time.sleep(1)
                player_hand.append(card)
                display_hand(player_hand, "Player")
                if calculate_hand_value(player_hand) > 21:
                    print(" You busted!")
                    time.sleep(1)
                    chips -= bet
                    continue
                action = 's'
            else:
                print("Not enough chips to double down.")
                time.sleep(1)
                continue

        while action == 'h':
            card = deck.pop()
            print(f"You drew: {card[0]} of {card[1]}")
            time.sleep(1)
            player_hand.append(card)
            display_hand(player_hand, "Player")
            if calculate_hand_value(player_hand) > 21:
                print(" You busted!")
                time.sleep(1)
                chips -= bet
                break
            action = input("Choose: (h)it or (s)tand: ").lower()
            time.sleep(1)

        if calculate_hand_value(player_hand) <= 21:
            print("\nDealer's Turn:")
            time.sleep(1)
            display_hand(dealer_hand, "Dealer")
            while calculate_hand_value(dealer_hand) < 17:
                card = deck.pop()
                print(f"Dealer draws: {card[0]} of {card[1]}")
                time.sleep(1)
                dealer_hand.append(card)
                display_hand(dealer_hand, "Dealer")

            player_total = calculate_hand_value(player_hand)
            dealer_total = calculate_hand_value(dealer_hand)

            print("\nEnd Results")
            time.sleep(1)
            display_hand(player_hand, "Player")
            display_hand(dealer_hand, "Dealer")

            if dealer_total > 21:
                print(" Dealer busted! You win! 😁")
                time.sleep(1)
                chips += bet
            elif player_total > dealer_total:
                print(" You win! 😁")
                time.sleep(1)
                chips += bet
            elif player_total < dealer_total:
                print("Dealer wins.")
                time.sleep(1)
                chips -= bet
            else:
                print("It's a tie!")
                time.sleep(1)

        if chips <= 0:
            print("You're out of chips. Game over :( .")
            time.sleep(1)
            break
        again = input("Play another round? (y/n): ").lower()
        time.sleep(1)
        if again != 'y':
            break

    print("🃏 Thankyou for playing Blackjack! 🃏")
    time.sleep(1)

if __name__ == "__main__":
    play_blackjack()
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for playing!🃏")
            break
