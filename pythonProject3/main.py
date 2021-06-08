import random
import os
import platform
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

'''The Card Class will create all the 52 cards using for loop'''
def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
class Cards:
    def __init__(self):
        self.cards = []
        for x in suits:
            for y in values.values():
                self.cards.append([x,y])
    def the_cards(self):
        return self.cards
'''The Player Class will Define the amount of chips they have, their name'''
class Player:
    def __init__(self,namez):
        self.name = namez
        self.chips = 50000
'''Deals with the Cards and is also playing against the player'''
class Dealer:
    def __init__(self):
        self.player_cards = []
        self.dealer_cards = []
BlackJack = True
while BlackJack:
    cards = Cards().cards
    dealer = Dealer()
    random.shuffle(cards)
    clear()
    name = input('Please enter your name: ')
    player = Player(name)

    while True:
        if len(dealer.player_cards) > 0:
            list.clear(dealer.player_cards)
            list. clear(dealer.dealer_cards)

        else:
            pass



        bet = input(f'\nYou have <{player.chips}> chips!\n\nHow much would you like to bet {player.name}: ')
        '''Another while loop to check if the amount inputted is an integer '''


        while True:



            try:
                player.chips = player.chips - int(bet)

                break
            except ValueError:
                print('ERROR: THAT\'S NOT A VALUE')
                bet = input('\nPlease try again: ')
                continue
        clear()
        print(f'\nBet accepted! your current balance is: <{player.chips}>')


        for x in cards:
            dealer.player_cards.append(cards.pop())
            dealer.player_cards.append(cards.pop())
            dealer.dealer_cards.append(cards.pop())
            dealer.dealer_cards.append(cards.pop())

            random.shuffle(cards)
            print(f'\n\n{player.name}\'s given cards: {dealer.player_cards[0::1]}\n\n\nDealer\'s given cards: {dealer.dealer_cards[0]}')


            dealer_sum = dealer.dealer_cards[0][1] + dealer.dealer_cards[1][1]
            player_sum = dealer.player_cards[0][1] + dealer.player_cards[1][1]

            hit_stand = input('\nDo you want to Hit or Stand [h][s]: ')
            if hit_stand == 's':


                print(f'\n\nThese were the Dealer\'s given cards{dealer.dealer_cards}')
                print(f'Dealer total: {dealer_sum}')
                print(f'your total: {player_sum}')
                if dealer_sum > 21:
                    print('You won!')
                    break
                elif player_sum > 21:
                    print('BUST!')
                    break
                elif dealer_sum > player_sum:
                    print('BUST')
                    break
                elif player_sum > dealer_sum:
                    print('You won!')
                    break

                elif dealer_sum == player_sum:
                    print('TIE!')
                    break




            elif hit_stand == 'h':
                dealer_sum = dealer.dealer_cards[0][1] + dealer.dealer_cards[1][1]
                player_sum = dealer.player_cards[0][1] + dealer.player_cards[1][1]
                print(f'Dealer total: {dealer_sum}')
                print(f'your total: {player_sum}')
                if dealer_sum > 21:
                    print('You won!')
                    break
                elif player_sum > 21:
                    print('BUST!')
                    break
                elif dealer_sum > player_sum:
                    print('BUST')
                    break
                elif player_sum > dealer_sum:
                    print('You won!')
                    break

                elif dealer_sum == player_sum:
                    print('TIE!')
                    break
            else:
                print('\nPlease only enter [h] to Hit or [s] to Stand ')
                continue




        val = input('do you want to play again[y][n]:')
        if val == 'y':
            clear()
            continue
        else:
            break
    break






