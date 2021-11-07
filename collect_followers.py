import os
import sys
import json
import time

# Collect all of the id's of the followers for Dr.Weigle's account
os.popen('twarc followers weiglemc > files/ids.txt')
time.sleep(3)

# collect user data from the original account
os.popen('twarc users weiglemc > files/friend_data.jsonl')

# collect user data from the id's of the followers and append to the file
os.popen('twarc users files/ids.txt >> files/friend_data.jsonl')

# Create a header for the csv file
header = open("files/followers.csv", 'w')
header.write("ID,SCREENNAME,FOLLOWERCOUNT\n")
header.close()

# Use the json user information and extract the id, screen name, and follower count. Print to file.
lines = sys.stdin.readlines()
for line in lines:
    tweet_data = json.loads(line)
    friend_id = tweet_data["id"]
    screen_name = tweet_data["screen_name"]
    follower_count = tweet_data["followers_count"]
    print(str(friend_id) + "," + screen_name + "," + str(follower_count))
