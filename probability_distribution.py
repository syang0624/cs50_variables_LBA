import matplotlib.pyplot as plt

def distribution(n):
    total_match = []
    napkins = percentage
    randomizer = percentage.copy()
    for i in range(n):
        napkins = percentage
        random.shuffle(randomizer)
        match_count = 0
        for j in range(len(napkins)):
            if napkins[j] == randomizer[j]:
                match_count += 1
        total_match.append(match_count)
    prob = []
    for k in range(len(napkins)):
        freq = total_match.count(k)
        prob.append(freq/n)
    plt.bar(range(len(prob)),prob)
    plt.ylabel("Probability")
    plt.xlabel("# of napkins")
    plt.show()
    
distribution(10000)
