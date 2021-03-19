import random

def EV(n):
    napkins = percentage
    randomizer = percentage.copy()
    total_match=0 #store total # of matches
    for i in range(n):
        napkins = percentage
        random.shuffle(randomizer)
        match_count = 0
        for j in range(len(napkins)):
            if napkins[j] == randomizer[j]:
                match_count += 1
        total_match += match_count
        
    return (total_match/n)

EV(10000)
