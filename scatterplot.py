data = pd.read_csv("Assignment 2 Data collection - Sheet2.csv") #import another spreadsheet for scatterplot
time = data["Time"]
day1 = data["% Day 1"]
day2 = data["% Day 2"]

#scatter plot coding
d1 = plt.scatter(time, day1, color = "b")
d2 = plt.scatter(time, day2, color = "r")
plt.legend((d1,d2),('Day 1', 'Day 2'),scatterpoints=1, loc='upper left', ncol=3, fontsize=8)


plt.title("Change in % of people who are wearing their masks incorrectly over time", fontsize = 15) 
plt.ylabel("%")
plt.xlabel("Time")
txt="Fig. 2. Data points were measured on different days.\n From 9AM to 5PM and 6:30PM share strong correlation.\n This correlation interpretation is limited because some of the data points were measured by a different observer and replaced data points measured on different day. \n The more data points with more days will give a better interpretation"
plt.figtext(0.5, -0.15, txt, wrap=True, horizontalalignment='center', fontsize=12)
fig = plt.gcf()
fig.set_figwidth(20)#increase the width to see a full scatterplot clearly
ax=plt.gca()
ax.set_facecolor('w')
plt.show()
