---
title: 'Calculating Distance Between Previous Colleges & BYU'
nav_exclude: true
---

As one of the variables of the dataset, I calculated distance (in miles) between the players' previous schools to BYU. I used this variable in the high school dataset, but calculating the distances involved me using a webpage over and over again. 

## `geopy` Package

When creating the transfer dataset, I discovered a Python package that made it much easier to calculate distances. This package is called `geopy`, and the function I used from it is called `geodesic`. It takes pairs of latitude and longitude coordinates and calculates the distance in whatever metric you choose.

Here is how you load in `geodesic`:

```python
from geopy.distance import geodesic
```

## Coordinates

Next, I used AI to find the latitude and longitude of each of the colleges the players in my dataset went to, as well as BYU. Here is a portion of that dictionary I created:

```python
schools = {
  'BYU': (40.25203, -111.64928), 
  'ASU': (33.42317, -111.92791),
  'Boise State': (43.60252, -116.20099), 
 ...
  'Washington': (47.60621, -122.33097),
  'Weber State': (41.24056, -111.98556),
  'Western Michigan': (42.26306, -85.58472),
}
```

## Using `geodesic`

Finally, I just plugged that dictionary into a `for` loop, using that `geodesic` function to create a dataset with the distance of each college from BYU. I did that by first creating a `distance_from_byu` function:

```python
def distance_from_byu(coords):
    byu_coords = schools['BYU']
    return geodesic(byu_coords, coords).miles
```

Notice how `geodesic` takes two arguments, and how I made one of the arguments automatically be BYU's coordinates. You can also see at the end that I wrote .`miles`, that's where you can specify the units of distance.

Then, I ran a `for` loop using that function to create a list of tuples, that I then used `pandas` to convert into a dataframe and export as a .csv file:

```python
rows = []

for school in schools:
    if school != 'BYU' and schools[school] != ():
        dist = distance_from_byu(schools[school])
        rows.append([school, round(dist, 2)])

distances = pd.DataFrame(rows, columns=['School', 'Distance'])
print(distances.head())
distances.to_csv('distances.csv', index=False)
```

## Conclusion

Calculating distances in this way was so much easier than what I did for the high school dataset. And, since I used latitude and longitude directly, the distance calculations were more precise than that website. I will definitely be using the `geopy` package again in the future!