import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Set style and configuration of bar plot
sns.set_style("whitegrid")
plt.figure(figsize=(20, 6))
plt.title("Twitter Friend Paradox - High Follower Count")

# Read in unsorted CSV, sort by highest friendcount
df = pd.read_csv("files/followers_high_count.csv")
sorted_df = df.sort_values(by=['FOLLOWERCOUNT'], ascending=False)

# Create a bar plot using Seaborn Library
ax = sns.barplot(x ="SCREENNAME", y='FOLLOWERCOUNT', data=sorted_df, log=True)
ax.set_yscale("log")
ax.set_xticklabels(ax.get_xticklabels(), fontsize=9,rotation=50,ha="right")
plt.tight_layout()
plt.show()


# mean median and std dev of follower count without orignial user account
original_df = pd.read_csv("files/followers_no_user.csv")
sorted_df = original_df.sort_values(by=['FOLLOWERCOUNT'], ascending=False)

# Save sorted dataframe to file
sorted_df.to_csv('files/sorted_twitter_followers.csv', index=False)

# Calculate the mean, std deviation and median of friendcount
mean = original_df['FOLLOWERCOUNT'].mean()
std_dev = original_df['FOLLOWERCOUNT'].std()
median = original_df['FOLLOWERCOUNT'].median()

print("Mean: ", round(mean, 3))
print("Standard Deviation: ", round(std_dev, 3))
print("Median: ", round(median, 3))
