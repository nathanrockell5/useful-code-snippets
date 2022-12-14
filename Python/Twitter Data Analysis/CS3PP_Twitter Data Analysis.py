# -*- coding: utf-8 -*-
"""CS3PP - Twitter Analysis (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TwwgLF0Sd2LQOQsarcpKQg5fcSNDfreM

### Module Code: CS3PY
### Assignment report Title: Twitter network map data extraction, pre-processing, and analysis 
### Student Number: 28009252, 26024679
### Date (when the work completed): 29/11/2021
### Actual hrs spent for the assignment:  Too many.
### Assignment evaluation (3 key points): 
- Interesting assignment touching on real life techniques and data analysis. 
- Deeper knowledge into Python and the vast range of libraries.

---

#### Twitter Accounts Analysed
- @Tim_Cook (Tim Cook, https://twitter.com/tim_cook) 
- @JoeBiden (Joe Biden, https://twitter.com/JoeBiden)
- @BorisJohnson (Boris Johnson, https://twitter.com/BorisJohnson)

---

# Task 1 - Data Gathering and Pre-processing
"""

import tweepy
# API Information
bearer_token = ''
api_key = ''
api_secret_key = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True)

"""This intial step is to set up the API connection so data can be pulled from Twitter. """

#Importing Relevant libraries
import pandas as pd
import numpy as np

"""### Pulling Tweets From User Accounts Into Dataframe"""

#Insert tweets into pandas dataframe and add other relevant columns
counter = 0
timCData = pd.DataFrame(columns=['User Name', 'Tweets', 'Followers', 'Date', 'Likes', 'RTs', 'Source'])
for tweet in tweepy.Cursor(api.user_timeline, screen_name='tim_cook', include_rts=False).items(300):
    timCData.loc[counter] = tweet.user.name, tweet.text, tweet.user.followers_count, tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.source
    counter+=1    

#Insert tweets into pandas dataframe and add other relevant columns
joeBData = pd.DataFrame(columns=['User Name', 'Tweets', 'Followers', 'Date', 'Likes', 'RTs', 'Source'])
for tweet in tweepy.Cursor(api.user_timeline, screen_name='joebiden', include_rts=False).items(300):
    joeBData.loc[counter] = tweet.user.name, tweet.text, tweet.user.followers_count, tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.source
    counter+=1
    
#Insert tweets into pandas dataframe and add other relevant columns
borisJData = pd.DataFrame(columns=['User Name', 'Tweets', 'Followers', 'Date', 'Likes', 'RTs', 'Source'])
for tweet in tweepy.Cursor(api.user_timeline, screen_name='borisjohnson', include_rts=False).items(300):
    borisJData.loc[counter] = tweet.user.name, tweet.text, tweet.user.followers_count, tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.source
    counter+=1 
    
frames = [timCData, joeBData, borisJData]

accountData = pd.concat(frames)

display(accountData)

"""The above code loops through the first 300 tweets for each account and appends the data to a dataframe. It includes key information like what account provided the tweet; number of followers; the number of likes and RTs, whilst also including the source.

Retweets were set to false as it was providing the RTs, however, these do not provide likes which brings down the average likes.

The 300 tweets from each of the account data frames are concatenated into one dataframe called accountData so that data analysis can be performed on the complete set.

This provided a further understanding of pandas dataframes and the Tweepy tweet object. Whilst also creating an opportunity to create the most efficient code with the least amount of loops as this could cause problems in the future if the aim was to pull thousands of tweets from many accounts.

### Pulling 100 Most Recent Followers From Each Account
"""

# Pull 100 recent followers from each account

# Insert follower screen names into pandas dataframe
counter = 0

timCFollowers = pd.DataFrame(columns=['User Name', 'Follower Name', 'Follower Id'])

for follower in tweepy.Cursor(api.get_followers, screen_name='tim_cook').items(100):
    #print(follower.screen_name)
    timCFollowers.loc[counter] = str('Tim Cook'), follower.screen_name, follower.id
    counter+=1

joeBFollowers = pd.DataFrame(columns=['User Name', 'Follower Name', 'Follower Id'])

for follower in tweepy.Cursor(api.get_followers, screen_name='joebiden').items(100):
    #print(follower.screen_name)
    timCFollowers.loc[counter] = str('Joe Biden'), follower.screen_name, follower.id
    counter+=1

borisJFollowers = pd.DataFrame(columns=['User Name', 'Follower Name', 'Follower Id'])

for follower in tweepy.Cursor(api.get_followers, screen_name='borisjohnson').items(100):
    #print(follower.screen_name)
    timCFollowers.loc[counter] = str('Boris Johnson'), follower.screen_name, follower.id
    counter+=1

    
frames = [timCFollowers, joeBFollowers, borisJFollowers]

followerData = pd.concat(frames)

display(followerData)

"""It was necessary to pull data on the usernames of recent followers of all three accounts in order to conduct network analysis.

---

# Task 2 - Exploratory Data Analysis

With the data collected from the 3 accounts, an Exploratory Data Analysis will be performed to compare information between the accounts so further understand the influence and interaction with the accounts and other users.
"""

import matplotlib.pyplot as plt

"""### Calculating Most Liked Tweets"""

#Most Liked Tweet
# print(np.max(accountData['Likes']))
display(accountData.loc[accountData['Likes'] == np.max(accountData['Likes'])])
mostLikes = accountData.sort_values(by='Likes', ascending=False)
mostLikes.head(10)

"""As seen from the results above that Joe Biden consistently gets more likes on average compared to the other 2 accounts.

### Calculating Most Retweeted Tweets
"""

#Most Retweeted Tweet
# print(np.max(accountData['RTs']))
display(accountData.loc[accountData['RTs'] == np.max(accountData['RTs'])])
mostRTs = accountData.sort_values(by='RTs', ascending=False)
mostRTs.head(10)

"""In this case Tim Cook and Joe Biden get a similar number of RTs consistently. However, Joe Biden has got the most retweeted tweet from the dataframe.

This could be down to the fact that Joe Biden has nearly three times the amount of followers, however, considering this, this shows that the engagement for Joe Biden's tweets is not as high as the other accounts as it would be expected that Joe Biden should consistently get a much higher RT count.

### Calculating Most Used Source
"""

#Most Used Source
print('Most used source for tweeting: ' + str(accountData.mode()['Source'][0]))

"""Considering that mobile phone usage has risen dramatically in the last decade and that 80% of users for Twitter use their mobile phone [3]. Therefore, it is a surprising figure that most of the tweets source are the Twitter Web App. 

However, it should be taken into consideration that these people/accounts live quite busy lifestyles and therefore may not have time to tweet or lack the knowledge, so those who are making these tweets would typically be marketing departments, and not the actual people themselves.

### Printing Number of Followers per Account
"""

#Number of followers
timCookFollowers = api.get_user(screen_name="tim_cook").followers_count
joeBidenFollowers = api.get_user(screen_name="joeBiden").followers_count
borisJohnsonFollowers = api.get_user(screen_name="borisJohnson").followers_count
print('Account Followers')
print('Tim Cook: ' + str(int(timCookFollowers)))
print('Joe Biden: ' + str(int(joeBidenFollowers)))
print('Boris Johnson: ' + str(int(borisJohnsonFollowers)))

"""### Calculating Average Number of Likes From Each Accounts 300 Tweets"""

#Average Likes Per Tweet
timCookAverageLikes = accountData['Likes'][accountData['User Name']=='Tim Cook'].mean()
joeBidenAverageLikes = accountData['Likes'][accountData['User Name']=='Joe Biden'].mean()
borisJohnsonAverageLikes = accountData['Likes'][accountData['User Name']=='Boris Johnson'].mean()
print("Average Likes")
print('Tim Cook: '+ str(int(timCookAverageLikes)))
print('Joe Biden: ' + str(int(joeBidenAverageLikes)))
print('Boris Johnson: ' + str(int(borisJohnsonAverageLikes)))

"""This code is used to find the average number of likes across the 300 tweets. This will be used later to show the average engagement from the followers for each account.

### Calculating Average Number of RTs From Each Accounts 300 Tweets
"""

#Average RTs Per Tweet
timCookAverageRTs = accountData['RTs'][accountData['User Name']=='Tim Cook'].mean()
joeBidenAverageRTs = accountData['RTs'][accountData['User Name']=='Joe Biden'].mean()
borisJohnsonAverageRTs = accountData['RTs'][accountData['User Name']=='Boris Johnson'].mean()
print("Average RTs")
print('Tim Cook: ' + str(int(timCookAverageRTs)))
print('Joe Biden: ' + str(int(joeBidenAverageRTs)))
print('Boris Johnson: ' + str(int(borisJohnsonAverageRTs)))

"""### Displaying Bar Graphs Representing Number of Followers, Average Likes and RTs"""

# Set Width of bars
barWidth = 0.25
 
# set heights of bars
bars1 = [timCookFollowers, joeBidenFollowers, borisJohnsonFollowers]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))

# Make the plot
plt.bar(r1, bars1, color='#FF0000', width=barWidth, edgecolor='white', label='Followers')

# Add xticks on the middle of the group bars
plt.xlabel('Account', fontweight='bold')
plt.ylabel('Followers * 10,000,000', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['Tim Cook', 'Joe Biden', 'Boris Johnson'])
 
# Create legend & Show graphic
plt.legend()
plt.show()

bars2 = [timCookAverageLikes, joeBidenAverageLikes, borisJohnsonAverageLikes]
bars3 = [timCookAverageRTs, joeBidenAverageRTs, borisJohnsonAverageRTs]

 
# Set position of bar on X axis
r2 = np.arange(len(bars1))
r3 = [x + barWidth for x in r1]

 
# Make the plot
# plt.bar(r1, bars1, color='#FF0000', width=barWidth, edgecolor='white', label='Followers')
plt.bar(r2, bars2, color='#00FF00', width=barWidth, edgecolor='white', label='Average Likes')
plt.bar(r3, bars3, color='#0000FF', width=barWidth, edgecolor='white', label='Average RTs')
 
# Add xticks on the middle of the group bars
plt.xlabel('Account', fontweight='bold')
plt.ylabel('Number of Likes/RTs', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['Tim Cook', 'Joe Biden', 'Boris Johnson'])
 
# Create legend & Show graphic
plt.legend()
plt.show()

"""From the graphs above, Joe Biden has a significantly higher number of followers compared to the other accounts, with also number of Average Likes and RTs being higher than the other accounts as well. 

It is also to take into consideration that on average accounts are mainly liking the accounts tweets rather than retweeting. 
"""

# Create data
g1 = (timCookFollowers, timCookAverageLikes)
g2 = (joeBidenFollowers, joeBidenAverageLikes)
g3 = (borisJohnsonFollowers, borisJohnsonAverageLikes)

data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("Tim Cook", "Joe Biden", "Boris Johnson")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
    
plt.xlabel('Followers * 10,000,000', fontweight='bold')
plt.ylabel('Number of Likes', fontweight='bold')
plt.title('Number of Likes Compared to Number of Followers')
plt.legend(loc=2)
plt.show()

# Create data
g1 = (timCookFollowers,timCookAverageRTs)
g2 = (joeBidenFollowers,joeBidenAverageRTs)
g3 = (borisJohnsonFollowers,borisJohnsonAverageRTs)

data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("Tim Cook", "Joe Biden", "Boris Johnson")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

plt.xlabel('Followers * 10,000,000', fontweight='bold')
plt.ylabel('Number of RTs', fontweight='bold')
plt.title('Number of RTs compared to Number of Followers')
plt.legend(loc=2)
plt.show()

"""From the data displayed above, it shows that on average, the more followers on the account, the more likes and RTs the account will get. However, this may not be strictly true so engagement needs to be taken into account to understand the percentage of users engaging with the profile.

### Calculating Engagement of followers
Below the code calculates the percentage of users that Like or RT a tweet on average, compared to how many followers the account has.
"""

timCookEngagementLikesP = (timCookAverageLikes/timCookFollowers)*100
joeBidenEngagementLikesP = (joeBidenAverageLikes/joeBidenFollowers)*100
borisJohnsonEngagementLikesP = (borisJohnsonAverageLikes/borisJohnsonFollowers)*100
print('Percentage of Like Engagement')
print('Tim Cook: %' + str(float(timCookEngagementLikesP)))
print('Joe Biden: %' + str(float(joeBidenEngagementLikesP)))
print('Boris Johnson: %' + str(float(borisJohnsonEngagementLikesP)))

print('---')

timCookEngagementRTP = (timCookAverageRTs/timCookFollowers)*100
joeBidenEngagementRTP = (joeBidenAverageRTs/joeBidenFollowers)*100
borisJohnsonEngagementRTP = (borisJohnsonAverageRTs/borisJohnsonFollowers)*100
print('Percentage of RT Engagement')
print('Tim Cook: %' + str(float(timCookEngagementRTP)))
print('Joe Biden: %' + str(float(joeBidenEngagementRTP)))
print('Boris Johnson: %' + str(float(borisJohnsonEngagementRTP)))

print('---')

timCookEngagementOverall = ((timCookAverageLikes + timCookAverageRTs)/timCookFollowers)*100
joeBidenEngagementOverall = ((joeBidenAverageLikes + joeBidenAverageRTs)/joeBidenFollowers)*100
borisJohnsonEngagementOverall = ((borisJohnsonAverageLikes + borisJohnsonAverageRTs)/borisJohnsonFollowers)*100
print('Percentage of Overall Engagement')
print('Tim Cook: %' + str(float(timCookEngagementOverall)))
print('Joe Biden: %' + str(float(joeBidenEngagementOverall)))
print('Boris Johnson: %' + str(float(borisJohnsonEngagementOverall)))

"""From the results above, eventhough the percentage is very low, on average Tim Cook's followers are more likely to Like and RT Tim Cooks content. 

Therefore, although the more followers an account has, typically there will be more likes and RTs overall. It doesn't necessarily mean the account will have the same amount of engagement compared to others. This could be down the the content being tweeted, or the nature of the followers. 

- Is the follower actively on Twitter? 
- Does the account want to like or RT the tweets or do they not see them on their feed? 

Using a network analysis, this should provide an insight into the influence of the accounts.

### Task 2 Conclusion
The main results to take from Task 2 are that: 
1. Joe Biden and Tim Cook get roughly the same number of likes and RTs per tweet, with the exception of a few tweets that achieved much higher numbers for Joe Biden
2. The number of followers an account directly correlates to how many likes and RTs the account gets.
3. Overall engagment is not consistent for all the accounts as eventhough Tim Cook has less followers than Joe Biden, on average Tim Cook gets more engagement on his tweets.

---

# Task 3 Network Analysis

Within this section, the aim is to create a network that represents the area of influence of the accounts.
"""

import networkx as nx
import csv

"""### Gathering Following Network"""

timCook = api.get_user(screen_name='tim_cook')
timCookFriends = api.get_friend_ids(screen_name = 'tim_cook')

csvFile = open('timCook.csv', 'a')
csvWriter = csv.writer(csvFile)
for friend in timCookFriends:
    fof = api.get_friend_ids(user_id=friend)
    csvWriter.writerow([api.get_user(user_id=friend).screen_name, str(fof)])

csvFile.close()

joeBiden = api.get_user(screen_name='joeBiden')
joeBidenFriends = api.get_friend_ids(screen_name = 'joeBiden')

csvFile = open('joeBiden.csv', 'a')
csvWriter = csv.writer(csvFile)
for friend in joeBidenFriends:
    fof = api.get_friend_ids(user_id=friend)
    csvWriter.writerow([api.get_user(user_id=friend).screen_name, str(fof)])

csvFile.close()

borisJohnson = api.get_user(screen_name='borisJohnson')
borisJohnsonFriends = api.get_friend_ids(screen_name = 'borisJohnson')

csvFile = open('borisJohnson.csv', 'a')
csvWriter = csv.writer(csvFile)
for friend in borisJohnsonFriends:
    fof = api.get_friend_ids(user_id=friend)
    csvWriter.writerow([api.get_user(user_id=friend).screen_name, str(fof)])

csvFile.close()

"""To create the area influence for the, the intial step is to get the list of accounts the account is followering, and then find their followers too. 

After these are retrieved from the for loop, the are written to a CSV file row-by-row.

### Displaying Network Graphs
"""

tcG = nx.read_adjlist("timCook.csv", create_using=nx.DiGraph)
nx.draw(tcG)
plt.show()

jbG = nx.read_adjlist("joeBiden.csv", create_using=nx.DiGraph)
nx.draw(jbG)
plt.show()

bjG = nx.read_adjlist("borisJohnson.csv", create_using=nx.DiGraph)
nx.draw(bjG)
plt.show()

"""Above are the graphs that are generated from the csv files. It shows the connections between the accounts that the user is following, and who they are following too.

### Finding Most Influential In Network
"""

tcMostInflu = nx.betweenness_centrality(tcG)
for w in sorted(tcMostInflu, key=tcMostInflu.get, reverse=True):
    print(w, tcMostInflu[w])
    
jbMostInflu = nx.betweenness_centrality(jbG)
for w in sorted(jbMostInflu, key=jbMostInflu.get, reverse=True):
    print(w, jbMostInflu[w])
    
jbMostInflu = nx.betweenness_centrality(bjG)
for w in sorted(jbMostInflu, key=bjMostInflu.get, reverse=True):
    print(w, bjMostInflu[w])

"""To find the most influencial account in the network. The betweenness centrality has to be found.

---

### References
- [1]: Rodolfo Ferro, 2 Oct 2017, https://github.com/RodolfoFerro/pandas_twitter/blob/master/01-extracting-data.md
- [2]: Gordon Macmillan, 24 Feb 2014, https://blog.twitter.com/en_gb/a/en-gb/2014/80-of-uk-users-access-twitter-via-their-mobile
- [3]: Python Graph Gallery, unknown, https://www.python-graph-gallery.com/11-grouped-barplot
- [4]: Python Spot, unknown, https://pythonspot.com/matplotlib-scatterplot/
"""

