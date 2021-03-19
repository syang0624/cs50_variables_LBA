
import matplotlib.pyplot as plt #importing matplotlib package
%matplotlib inline
#histogram coding
plt.hist(percentage, bins = [0,10,20,30,40,50,60,70,80,90,100], color = "r", alpha=1, linewidth=5)
plt.title("Distribution of percentage of people who are wearing their masks incorrectly.", fontsize = 15)
plt.xlabel("Percentage (%)", fontsize = 10)
plt.ylabel("Frequency of data", fontsize = 10)
txt="Fig. 1. 40 Data points are collected in this histogram.\n There are 10 bins in this histgoram and all data points are distributd in each bin.\nThis histogram is slightly skewed to the left." 
plt.text(45,-3,txt, horizontalalignment = "center")
plt.xticks([0,10,20,30,40,50,60,70,80,90,100]) #increase xticks by 10
plt.yticks([0,1,2,3,4,5,6,7,8,9]) #increase yticks by 1
plt.axvline(mean(percentage), color='g', label = "Mean = 38.25") #label legend for mean
plt.axvline(median(percentage), color='y', label = "Median = 38.75")#label legend for median
plt.legend()
ax=plt.gca()
ax.set_facecolor('w')
plt.show()
