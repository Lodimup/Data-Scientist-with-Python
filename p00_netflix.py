"""
Solutions to the DataCamp
Project: Investigating Netflix Movies and Guest Stars in The Office
Imports are moved to their appropriate places.
"""
import pandas as pd
import matplotlib.pyplot as plt

# 1
years = [i for i in range(2011, 2020+1)]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
movie_dict = {
    'years': years,
    'durations': durations,
}
print(movie_dict)

# 2
durations_df = pd.DataFrame(movie_dict)
print(durations_df)

# 3
fig = plt.figure()
plt.plot(durations_df['years'], durations_df['durations'])
plt.title('Netflix Movie Durations 2011-2020')
plt.show()

# 4
netflix_df = pd.read_csv('datasets/netflix_data.csv')
print(netflix_df.head(5))

# 5
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]
print(netflix_movies_col_subset.head(5))

# 6
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'])
plt.title('Movie Duration by Year of Release')
plt.show()

# 7
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]
print(short_movies.head(20))

# 8 DataCamp's solution
# colors = []
# for _, row in netflix_movies_col_subset.iterrows():
#     if row['genre'] == "Children":
#         colors.append("red")
#     elif row['genre'] == "Documentaries":
#         colors.append("blue")
#     elif row['genre'] == "Stand-Up":
#         colors.append("green")
#     else:
#         colors.append("black")
# print(colors[:10])

# Better solution to 8
def assign_color(genre: str) -> str:
        if genre == 'Children':
            return 'red'
        if genre == "Documentaries":
            return 'blue'
        if genre == "Stand-Up":
            return 'green'

        return 'black'


netflix_movies_col_subset['colors'] = netflix_movies_col_subset['genre'].apply(assign_color)
colors = list(netflix_movies_col_subset['colors'])
print(colors[:20])

# 9
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c=netflix_movies_col_subset['colors'])
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()

# 10
are_movies_getting_shorter = 'No'
