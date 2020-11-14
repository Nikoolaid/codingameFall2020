import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
allSpells = []
allPotions = []
inventory = []

# game loop
while True:
    action_count = int(input())  # the number of spells and recipes in play

    for i in range(action_count):
        # action_id: the unique ID of this spell or recipe
        # action_type: in the first league: BREW; later: CAST, OPPONENT_CAST, LEARN, BREW
        # delta_0: tier-0 ingredient change
        # delta_1: tier-1 ingredient change
        # delta_2: tier-2 ingredient change
        # delta_3: tier-3 ingredient change
        # price: the price in rupees if this is a potion
        # tome_index: in the first two leagues: always 0; later: the index in the tome if this is a tome spell, equal to the read-ahead tax
        # tax_count: in the first two leagues: always 0; later: the amount of taxed tier-0 ingredients you gain from learning this spell
        # castable: in the first league: always 0; later: 1 if this is a castable player spell
        # repeatable: for the first two leagues: always 0; later: 1 if this is a repeatable player spell
        action_id, action_type, delta_0, delta_1, delta_2, delta_3, price, tome_index, tax_count, castable, repeatable = input().split()
        action_id = int(action_id)
        delta_0 = int(delta_0)
        delta_1 = int(delta_1)
        delta_2 = int(delta_2)
        delta_3 = int(delta_3)
        price = int(price)
        tome_index = int(tome_index)
        tax_count = int(tax_count)
        castable = castable != "0"
        repeatable = repeatable != "0"
        array=[action_id, action_type, delta_0, delta_1, delta_2, delta_3, price, tome_index, tax_count, castable, repeatable]
        if str(action_type) == "BREW" :  
            allPotions.append(array)
        elif str(action_type) == "CAST": 
            allSpells.append(array)
    for i in range(2):
        # inv_0: tier-0 ingredients in inventory
        # score: amount of rupees
        inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]
        inventory = [inv_0, inv_1, inv_2, inv_3, score]
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
    print("BREW " + str(action_id))


def add0():
    return 'CAST ' + str(allSpells[0][0])

def add1():
    thingToCast = allSpells[1][0]
    if inventory[0] < 1:
        thingToCast = allSpells[0][0]
    return 'CAST ' + str(thingToCast)

def add2():
    thingToCast = allSpells[2][0]
    if inventory[1] < 1:
        thingToCast = allSpells[1][0]
    return 'CAST ' + str(thingToCast)

def add3():
    thingToCast = allSpells[3][0]
    if inventory[2] < 1:
        thingToCast = allSpells[2][0]
    return 'CAST ' + str(thingToCast)

def potionCost(): #returns array of all potion costs (materials consumed)
    t0 = None
    t1 = None
    t2 = None
    t3 = None
    allCosts = []
    for potion in allPotions:
        t0 = potion[2] * -1 # num tier 0 ingredients * cost
        t1 = potion[3] * -2
        t2 = potion[4] * -3
        t3 = potion[5] * -4
        allCosts.append(t0+t1+t2+t3) #add sum of costs for each potion to array of costs 
    return allCosts #returns array of total costs
    
def potionWorth(): #returns an array of all potions' price return / material costs
    prices = []
    costs = potionCost()
    worths = []
    for potion in allPotions: #for each potioin, add the price of the potioin to pricce array
        price.append(potion[6]) 
    for i in range(len(prices)-1): #then, calculates and adds to worths array all potion worths/scores
        worths[i] = price[1]/costs[i]
    return worths

def getHighest(): #returns highest in 
    highest = potionWorth()
    for i in allPotions:
        if potionWorth() > highest :
            highest=i[0] #sets highest equal to the actionID of the best cost potion
    return highest #return actionID of highest potion 

def canMake(): #2345 are inv slots
    if spell[2] > inv[0]: #if u need more 0, add 0
        add0()
    elif spell[3] > inv[1]: #if u need more 1, add 1
        add1()
    elif spell[4] > inv[2]: # so on ...
        add2()
    elif spell[5] > inv[3]:
        add3()
    else: #if you dont need anything, brew what u want !!
            print("BREW " + getHighest(allPotions)
