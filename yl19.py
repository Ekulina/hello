import random

dealer_cards = []
player_cards = []

# jaga kaardid
# näita kaarte

# diileri kaardid
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint (1, 11))
    if len(dealer_cards) ==2:
        print("Diileri kaardid on X &", dealer_cards[1])

# mängija kaardid
while len(player_cards) != 2:
    player_cards.append(random.randint (1, 11))
    if len(player_cards) ==2:
        print("Sinu kaardid on ", player_cards)

# diileri kaartide summa
if sum(dealer_cards) == 21:
    print("Diileril on 21 ja ta võidab!")
elif sum (dealer_cards) > 21:
    print("Diiler läks lõhki!")

# mängija kaartide summa
while sum(player_cards) < 21:
    action_taken = str(input("Kas sa tahad passida või juurde? "))
    if action_taken == "juurde":
        player_cards.append(random.randint(1, 11))
        print("Sul on nüüd summa kokku " + str(sum(player_cards)) + " nendest kaartidest ", player_cards)
    else:
        print("Diileril nüüd summa kokku " + str(sum(dealer_cards)) + " nendest kaartidest ", dealer_cards)
        print("Sul on summa kokku " + str(sum(player_cards)) + " nendest kaartidest ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Diiler võitis!")
        else:
            print("Sina võitsid!")
            break
if sum(player_cards) > 21:
    print("Läksid lõhki! Diiler võitis!")
elif sum(player_cards) == 21:
    print ("Sul on Blackjack! Sa võitsid!" )