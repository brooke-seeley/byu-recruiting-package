---
title: 'Scraping Top 247 Lists'
parent: "Dataset Building"
nav_order: 1
---

One of the variables in my dataset is called `247Top`. Its values are `Y` for being in the top 247 players for that year according to [247Sports](https://247sports.com) in their respective categories (High School, Junior College, Transfer Portal), and `N` if they were not on that list.

I already had a list of players that BYU was interested in/offered to each year in the transfer portal or junior college, but I wanted a quicker way to check if they were on the top 247 list and get their info right away. I decided to scrape the webpage!

## Required Packages

I had to load a few packages to scrape these webpages:

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup
```

`requests` and `bs4` were loaded to scrape the webpages itself, and `pandas` was used to convert the dictionaries the scraping created into dataframes.

## Transfer Portal Data

I will be giving you an example of how I scraped the top 247 transfers from each year using 2023. I started by scraping the html for each player on the list:

```python
twothree_transfers_url = 'https://247sports.com/season/2023-football/transferportaltop/'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

twothree_response = requests.get(twothree_transfers_url, headers=headers)
twothree_soup = BeautifulSoup(twothree_response.text, "html.parser")

players = twothree_soup.find_all('li', class_='transfer-player')
```

Next, I created a dictionary and used a `for` loop to fill it. I found the first name, last name, height, weight, and composite score of each player by using the tags and classes from the html:

```python
twothree_data = {'First': [], 'Last': [], 'Height': [], 'Weight': [], 'Score': []}

for player in players:
    name_tag = player.find('h3').find('a')
    if name_tag:
        name = name_tag.text.strip().split()
        first = name[0]
        last = name[-1]
    else:
        first = last = None
    bio_tag = player.find('div', class_='bio')
    if bio_tag:
        hw = bio_tag.text.strip().replace('\n','').split('/')
        if len(hw) == 2:
            height = hw[0].strip()
            weight = hw[1].strip()
        else:
            height = weight = None
    else:
        height = weight = None
    score_tag = player.find('div', class_='rating')
    score = score_tag.text.strip() if score_tag else None
    twothree_data['First'].append(first)
    twothree_data['Last'].append(last)
    twothree_data['Height'].append(height)
    twothree_data['Weight'].append(weight)
    twothree_data['Score'].append(score)
```

Then, I converted that dictionary into a dataframe, checked that the length was 247, and sorted the data by last name before converting it to a .csv file:

```python
twothree_df = pd.DataFrame(twothree_data)
print(twothree_df.head())
print(len(twothree_df))
twothree_transfer = twothree_df.sort_values(by = 'Last')
twothree_transfer.to_csv('transfer_datasets/twothree_transfer.csv', index=False)
```

I then used that file and compared it to the list of transfers that BYU was interested in from that year to find matches. If there was a match, I filled in `247Top` with `Y` and filled in the players' heights, weights, and composite scores. I did this for each year, and any (non-JC) player that wasn't on these lists had a `N` filled in.

## Junior College Data

The html of the top junior college (abbreviated as JC) data was similar to the transfer list, but gave another challenge. The start of the scraping was similar, with a base url and headers for each year. The dictionary and how I filled it in was also the same as before.

The challenge for the JC data came from how the page only displayed 50 players at a time. So, for scraping, instead of a `for` loop for the dictionary creation, it was instead a function called `create_data`. The `for` loop I used came from looping through the pages of 50, since you had to click "Load More Players" at the bottom of the page. 

I had the pages loop 5 times to catch 250 players. Here is the loop, you can see that it includes the `BeautifulSoup` and `find_all` functions before plugging in those players into the `create_data` function:

```python
for page in range(1, 6):
    url = twothree_base_url + str(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    players = soup.find_all('li', class_='rankings-page__list-item')
    create_data(players)
```

The rest of the process was just like with the tranfer data. I converted it to a `pandas` dataframe, sorted and exported as a .csv file, and compared it to the list I already had before filling in `247Top`.

Next, check out [Non-Top Player Scraping](./non_top_pages.md)