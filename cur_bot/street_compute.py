import eval7
import itertools
import pandas as pd

def calculate_strength(hole, iters, board, street):
        '''
        A Monte Carlo method meant to estimate the win probability of a pair of 
        hole cards given board cards. Simlulates 'iters' games and determines the win rates of our cards

        Arguments:
        hole: a list of our two hole cards
        iters: a integer that determines how many Monte Carlo samples to take
        board: cards on the board
        street: 0, 3, 4, 5 tells how many cards on the board. NOTE PROBABLY ONLY NEED 3,4,5

        Return:
        Strength of hand + board cards
        '''
        deck = eval7.Deck() #eval7 object!
        hole_cards = [eval7.Card(card) for card in hole] #card objects, used to evaluate hands
        board_cards = [eval7.Card(card) for card in board] #card objects, used to evaluate hands
        

        for card in hole_cards: #remove cards that we know about! they shouldn't come up in simulations
            deck.cards.remove(card)

        for card in board_cards: #remove cards that we know about! they shouldn't come up in simulations
            deck.cards.remove(card)

        score = 0

        for _ in range(iters): #take 'iters' samples
            deck.shuffle() #make sure our samples are random

            _COMM = 5 #the number of cards we need to draw
            _OPP = 2
            board = street # the number of cards on the table

            draw = deck.peek(_COMM + _OPP - board)

            opp_hole = draw[: _OPP]
            community = draw[_OPP: ] + board_cards

            our_hand = hole_cards + community #the two showdown hands
            opp_hand = opp_hole + community

            our_hand_value = eval7.evaluate(our_hand) #the ranks of our hands (only useful for comparisons)
            opp_hand_value = eval7.evaluate(opp_hand)

            if our_hand_value > opp_hand_value: #we win!
                score += 2
            
            elif our_hand_value == opp_hand_value: #we tie.
                score += 1
            
            else: #we lost....
                score += 0
        
        hand_strength = score / (2 * iters) #this is our win probability!

        return hand_strength

def street_strength(cards, street):
    '''
    RETURN:
        Scoring:
    9 - Flush (Straight all in same suit)
    8 - Four of a kind
    7 - Full house 
    6 - Flush (All same suit)
    5 - Straight (sequential)
    4 - Three of a kind
    3 - two pairs
    2 - one pair
    1 - high card
    '''
    suits ={}
    ranks = {}

    #Get frequencies
    for card in cards:
        if card[1] not in suits:
            suits[card[1]] = card
        else:
            suits[card[1]] = card
        
        if rank_to_numeric(card[0]) not in ranks:
            ranks[rank_to_numeric(card[0])] = card
        else:
            ranks[rank_to_numeric(card[0])] = card
    
    #Find pairs
    pairs = [] #keep track of all of the pairs we identified
    singles = [] #all other cards
    for rank in ranks:
        cards = ranks[rank]

        if len(cards) == 1: #single card, can't be in a pair
            singles.append(cards[0])
        
        elif len(cards) == 2 or len(cards) == 4: #a single pair or two pairs can be made here, add them all
            pairs += cards
        
        else: #len(cards) == 3  A single pair plus an extra can be made here
            pairs.append(cards[0])
            pairs.append(cards[1])
            singles.append(cards[2])
    
    #Find if ranks are sequential
    rank_seq = sorted(ranks.keys()) == list(range(min(ranks.keys()), max(ranks.keys())+1))

    #Find sizes of pairs / ranks
    suit_size = {suit: len(suits[suit]) for suit in suits}

    if rank_seq and max(suit_size.values()) == 5:
        return 9
    elif max(.values()) == 4:
        return 8
    elif 
    


def rank_to_numeric(rank):
        '''
        Method that converts our given rank as a string
        into an integer ranking

        rank: str - one of 'A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'
        '''
        if rank.isnumeric(): #2-9, we can just use the int version of this string
            return int(rank)
        elif rank == 'T': #10 is T, so we need to specify it here
            return 10
        elif rank == 'J': #Face cards for the rest of them
            return 11
        elif rank == 'Q':
            return 12
        elif rank == 'K':
            return 13
        else: #Ace (A) is the only one left, give it the highest rank
            return 14

    
'''''

'''''
    

if __name__ == '__main__':
    _STREET = 3
    _MONTE_CARLO_ITERS = 5000
    _RANKS = 'AKQJT98765432' 
    _SUITS = 'cdsh'
    _CARDS = [rank + suit for rank in _RANKS for suit in _SUITS]

    board_cards = list(itertools.combinations(_CARDS, _STREET)) #all possible board cards
    holes = list(itertools.combinations(_CARDS, 2)) #all holes we can have

    all_strengths = [] 
    all_cards = []

    for hole in holes:
        for board in board_cards:
            if not any(card in board for card in hole):
                print(hole+board)
                all_strengths.append(calculate_strength(hole, _MONTE_CARLO_ITERS, board, _STREET))
                all_cards.append(hole[0] + hole[1] + board[0] + board[1] + board[2])

    '''
    suited_strengths = [calculate_strength([hole[0] + 'c', hole[1] + 'c'], _MONTE_CARLO_ITERS) for hole in off_rank_holes] #all holes with the same suit
    off_suit_strengths = [calculate_strength([hole[0] + 'c', hole[1] + 'd'], _MONTE_CARLO_ITERS) for hole in off_rank_holes] #all holes with off suits
    pocket_pair_strengths = [calculate_strength([hole[0] + 'c', hole[1] + 'd'], _MONTE_CARLO_ITERS) for hole in pocket_pair_holes] #pocket pairs must be off suit

    suited_holes = [hole[0] + hole[1] + 's' for hole in off_rank_holes] #s == suited
    off_suited_holes = [hole[0] + hole[1] + 'o' for hole in off_rank_holes] #o == off-suit
    pocket_pairs = [hole[0] + hole[1] + 'o' for hole in pocket_pair_holes] #pocket pairs are always off suit

    all_strengths = suited_strengths + off_suit_strengths + pocket_pair_strengths #aggregate them all
    all_holes = suited_holes + off_suited_holes + pocket_pairs
    '''

    hole_df = pd.DataFrame() #make our spreadsheet with a pandas data frame!
    hole_df['Cards'] = all_cards
    hole_df['Strengths'] = all_strengths

    hole_df.to_csv('flop_strengths.csv', index=False) #save it for later use, trade space for time!

