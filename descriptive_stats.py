#define mean function
def mean(lst):
    mean = sum(lst) / len(lst)
    return mean

#median calculation
def median(lst):
    lst.sort()
    if len(lst) % 2 == 0: # Finding the position of the median if the # of elements is even
        first_median = lst[len(lst) // 2]
        second_median = lst[len(lst) // 2 - 1]
        median = (first_median + second_median) / 2
    else: # Finding the position of the median if the # of elements is odd
        median = lst[len(lst) // 2]
    return median

#mode calculation
def mode(lst):
    L1=[] #count the occurrence of each number and append or add findings to the list
  
    i = 0 #count the numbers and put them into L1
    while i < len(lst) : 
        L1.append(lst.count(lst[i])) 
        i += 1

    # the occurrences for each number in sorted lst 
    # create a custom dictionary d1 for k : V 
    # k = value, v = occurence

    d1 = dict(zip(lst, L1))  
    d2={k for (k,v) in d1.items() if v == max(L1)} # the k values with the highest v values. 
    return str(d2)

#range calculation
def rng(lst):
    return max(lst)-min(lst)#range is equal to maximum vlaue - minimum value

#standard deviation calculation
def standard_dev(lst):
    variance = sum([((x - mean(lst)) ** 2) for x in lst]) / len(lst) #interpret the formula for standard deviation
    sd = variance ** 0.5 #sqrt
    return sd

print("Mean is:", round(mean(percentage),2))
print("Median is:", median(percentage))
print("Modes are:", mode(percentage))
print("Range is:", rng(percentage))
print("Standard Deviation is:", round(standard_dev(percentage),2))
