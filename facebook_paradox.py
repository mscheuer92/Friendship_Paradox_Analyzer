import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set style and configuration of bar plot
sns.set_style("whitegrid")
plt.figure(figsize=(20, 8))
plt.title("Facebook Friend Paradox")

# Read in unsorted CSV and get the number of friends for the user
df = pd.read_csv("HW4-friend-count.csv")
user_friendcount = len(df) + 1 # add +1 to account for element 0

# Search for original user in file (in case script has been run more than once),
# and add it to the file if it's not there.
with open('files/fb_friend_count.csv') as f:
    if 'ORIGINAL_USER,99' not in f.read():
        fb_friend = open('files/fb_friend_count.csv', 'a')
        fb_friend.write("ORIGINAL_USER,"+str(user_friendcount))
        fb_friend.close()

# Read in updated file
new_df = pd.read_csv("files/fb_friend_count.csv")
sorted_df = new_df.sort_values(by=['FRIENDCOUNT'], ascending=False)

# # Create a bar plot using Seaborn Library
ax = sns.barplot(x='USER', y='FRIENDCOUNT', data=sorted_df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
plt.tight_layout()
plt.show()


# Gather data from file that does not include the user and calculate the mean, median, and standard deviation of the friends.
original_df = pd.read_csv('HW4-friend-count.csv')

mean = original_df['FRIENDCOUNT'].mean()
std_dev = original_df['FRIENDCOUNT'].std()
median = original_df['FRIENDCOUNT'].median()

print("Mean: ", round(mean, 3))
print("Standard Deviation: ", round(std_dev, 3))
print("Median: ", round(median, 3))



# Save sorted dataframe that includes the user to file for viewing
sorted_df.to_csv('files/sorted_facebook_friends.csv', index=False)



