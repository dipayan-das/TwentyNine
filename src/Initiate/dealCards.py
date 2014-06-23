'''
Created on Jun 10, 2014

@author: Dibyendu
'''

import random, collections

def DealHand(playDeck):        #Deals 8 cards from the playDeck to computer_player
    computer_player = random.sample(playDeck, 8)
    for card in computer_player:
        playDeck.remove(card)
    return (computer_player, playDeck)

def DealHands(playDeck):      # Deals cards to all four players and returns the hands
    hands = []
    for _ in range(4):
        pl = DealHand(playDeck)
        hands.append(pl[0])
        playDeck = pl[1]
    return hands
    

def RotatePlayers(players):     #Rotates the players so that the starting player is positioned at start of list
    starting_player = raw_input("Enter the number of the starting player : ")
    temp = collections.deque(players)
    temp.rotate(4 - starting_player + 1)
    players = list(temp)
    return players