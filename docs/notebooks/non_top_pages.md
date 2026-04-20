---
title: 'Scraping Players NOT on Top 247 Lists'
---

This was one of the more interesting scraping challenges as part of this project. I still wanted to grab the same info that I did for the top 247 players (height, weight, composite score), but there was not one simple page I could scrape that from.

## Position Keys

I noticed that from a player's page, you could see if they were ranked in their *position* as a transfer (there were so few JC players that I just got their data manually). When you clicked on their position ranking, it took you to a page of the top 247 players for that *position* for that year.

I took a look at the url, and it was in this format:

https://247sports.com/season/[year]-football/TransferPortalTop/?positionKey=[key]

Each position had its own two-digit key, that when inputted into this url, took you to the top 247 list for that position. I went through each key and found the following:

* 9 - PRO
* 12 - RB
* 14 - WR
* 15/68 - TE (changed from 15 to 68 after a couple years)
* 16 - OT
* 17 - OG
* 20 - SDE
* 22 - ILB
* 24 - CB
* 25 - S
* 26 - ATH
* 27 - K
* 37 - P
* 38 - LS
* 57 - QB
* 58 - IOL
* 59 - LB
* 60 - EDGE
* 61 - DL

## Finding Players

With this newfound information, I went through each year and position key, searching for players that matched my list of players BYU was interested in. I noted their ranking on the page, and created a dictionary from this. The dictionary had three parts:

* Year (2023-2026)
* Position Key
* Rankings (of the players in that position key)

Here's a portion of that dictionary:

```python
config = {
    2023: {
        '24': [101,104],
        '61': [56,94,42,66],
        '60': [29],
        '58': [23,56,51],
        '59': [36],
        '16': [50,77,22,28,32],
        '57': [19,26,21],
        '12': [54,32],
        '15': [18],
        '14': [125]
    },
...
    2026: {
        '24': [3,176],
        '59': [126],
        '58': [63,23],
        '16': [134],
        '68': [17],
        '14': [58,144]
    }
}
```

## Building the Function

This dictionary allowed me to create a function that edited the url with the year and position key, find the players associated with each ranking, and build a dictionary with the players' names, heights, weights, and composite scores.

I imported the following packages for scraping and converting to a dataframe, and set headers for scraping:

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0'
}
```

I then created a function called `scrape_position` that took the arguments from the dictionary (year, position key, rankings). The function edited the base url based on the year and position key and found the players associated with the rankings, like this:

```python
for player in players:
        rank_tag = player.find('div', class_='playerRank')
        if rank_tag:
            rank = int(rank_tag.text.strip())
        else:
            continue
        if rank not in ranks:
            continue
```

The rest of the function, to gather the data I wanted, was very similar to the function of top 247 player pages I scraped before (see the page where I explained how I scraped those for more information).

## Creating the Dataset

Now, I just had to create a `for` loop where I went through the dictionary to get the list of players I needed (and their data):

```python
all_data = {'First': [], 'Last': [], 'Year': [], 'Height': [], 'Weight': [], 'Score': []}

for year in config:
    for position in config[year]:
        
        ranks = config[year][position]
        
        temp = scrape_position(year, position, ranks)
        
        for i in range(len(temp['First'])):
            all_data['First'].append(temp['First'][i])
            all_data['Last'].append(temp['Last'][i])
            all_data['Year'].append(year)
            all_data['Height'].append(temp['Height'][i])
            all_data['Weight'].append(temp['Weight'][i])
            all_data['Score'].append(temp['Score'][i])
```

Finally, I converted this to a `pandas` dataframe, changed the height to inches, sorted by year and last name, and exported to a .csv file. Everything I needed was right there!

## Conclusion

Scraping in this way was so fun to build, and I felt proud of myself for finding the position key pattern. It solved this problem of going to each player's page over and over, instead giving me all of the data I needed in one `for` loop.

Next, check out [Distance Calculation](notebooks\distance_calc.md)