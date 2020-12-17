'''
Code to display graphs and find statistics about the data
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

followers = []

# open follower count file and add every value to a lit
readfollowers = open("Data/FollowerCts.txt", "r")
for x in readfollowers:
    followers.append(int(x))

# find mean, median, mode, range, and outliers
followersnp = np.array(followers)
mean = np.mean(followersnp)
median = np.median(followersnp)
mode = stats.mode(followersnp)
maximum = np.amax(followersnp)
followerrange = np.ptp(followersnp)
outliers = []
for i in followersnp:
    if i > 3701:
        outliers.append(i)


print("mean:", mean,"median:",  median, "mode:",mode[0],mode[1], "range:", followerrange, "max:", maximum)
print(outliers)

# create a histogram
plt.figure(1)
# np.clip reduces all values above 3750 to one bin to minimize the size of the histogram
plt.hist(np.clip(followersnp, 0, 3750), bins=np.arange(0, 4000, 250), histtype = "stepfilled")
plt.ylabel("Frequency")
plt.xlabel("Number of Followers")
plt.title("Histogram of Followers")
# set x and y axis ranges
plt.xticks(np.arange(0, 3750, 250))
plt.yticks(np.arange(0,1000, 20))
plt.ylim([0, 550])
plt.grid(True)
plt.show()

# create a boxpot of values (excluding outliers)
plt.figure(2)
boxPlotValues = plt.boxplot(followersnp, showfliers = False, vert=False)
# adding labels for five number summary
for line in boxPlotValues['medians']:
    # get position data for median line
    x, y = line.get_xydata()[1] # top of median line
    # overlay median value
    plt.text(x, y, '%.1f' % x,
         horizontalalignment='center') # draw above, centered

for line in boxPlotValues['boxes']:
    x, y = line.get_xydata()[0] # bottom of left line
    plt.text(x,y, '%.1f' % x,
         horizontalalignment='center', # centered
         verticalalignment='top')      # below
    x, y = line.get_xydata()[3] # bottom of right line
    plt.text(x,y, '%.1f' % x,
         horizontalalignment='center', # centered
             verticalalignment='top')      # below

for line in boxPlotValues['caps']:
    x, y = line.get_xydata()[0] # bottom of left line
    plt.text(x,y, '%.1f' % x,
         horizontalalignment='center',
            verticalalignment="top")      # below

plt.xlabel("Number of Followers")
plt.title("Boxplot of Followers")
plt.show()

# finding percentages for pie chart
first = 0
second = 0
third = 0
fourth = 0
total = 0
for i in followersnp:
    if i <= 1000:
        first += 1
    elif i <= 10000:
        second += 1
    elif i <= 100000:
        third += 1
    else:
        fourth += 1
    total += 1
plt.figure(3)
labels = ["1-1000 Followers", "1,001-10,000 Followers", "10,001-100,000 Followers", "100,001+ Followers"]
values = [(first/total)*100, (second/total)*100, (third/total)*100, (fourth/total)*100]
plt.pie(values, labels = labels, autopct='%1.1f%%')
plt.title("Piechart of Followers")
plt.show()
