import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")
plt.figure(figsize=(20, 6))
plt.title("Twitter Friend Paradox - Low Follower Count")

# Read in unsorted CSV, sort by highest friendcount
df = pd.read_csv("files/followers_low_count.csv")
sorted_df = df.sort_values(by=['FOLLOWERCOUNT'], ascending=False)

# Create a bar plot using Seaborn Library
ax = sns.barplot(x ="SCREENNAME", y='FOLLOWERCOUNT', data=sorted_df)

ax.set_xticklabels(ax.get_xticklabels(), fontsize=5,rotation=50,ha="right")
plt.tight_layout()
plt.show()
