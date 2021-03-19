import random

napkins = percentage
randomizer = percentage.copy() #copy the list


totalnomatches = 0
for i in range(10000): #10,000 rounds of simulation!
    count_dismatch = 0
    random.shuffle(randomizer) #shuffle the copied list
    for j in range(len(napkins)):
        if napkins[j] != randomizer[j]: #when the original set is not matched with shuffled set
            count_dismatch += 1
    if count_dismatch == len(napkins):
        totalnomatches += 1
#if two napkins for two distinct measurements show the same value, and are then swapped, they are lucky match.

print((totalnomatches / 10000) * 100,"%")
