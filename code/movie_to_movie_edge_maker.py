import json
import csv
import copy

movie_cast_director = {}
with open('data/json/movie_cast_director_json.txt') as json_file:
    data = json.load(json_file)
    movie_cast_director = data

movie_to_movie = {}
empty_movies = {}

for movie in movie_cast_director:
    empty_movies[movie] = 0

for movie in movie_cast_director:
    movie_to_movie[movie] = copy.deepcopy(empty_movies)

for source in movie_cast_director:
    for target in movie_cast_director:
        if movie_cast_director[source]["director"] == movie_cast_director[target]["director"]:
            movie_to_movie[source][target] += 5
        for actor in movie_cast_director[source]["cast"]:
            if actor in movie_cast_director[target]["cast"]:
                movie_to_movie[source][target] += 1

movies = []

for movie in movie_cast_director:
    movies.append(movie)

#csv write
# edge list
f = open('data/csv/movies_edges.csv', 'w', newline='')
writer = csv.writer(f)
header=["Source", "Target", "Weight", "Label"]
writer.writerow(header)
for i in range(len(movie_to_movie)):
    for j in range(len(movie_to_movie)-i):
        if movie_to_movie[movies[i]][movies[j]] > 0 and movies[i] != movies[j]:
            line = [movies[i], movies[j] ,movie_to_movie[movies[i]][movies[j]],movie_to_movie[movies[i]][movies[j]]]
            writer.writerow(line)
f.close()

f = open('data/csv/movies_list.csv', 'w', newline='')
writer = csv.writer(f)
header=["Id", "Label"]
writer.writerow(header)
for movie in movies:
    line = [movie,movie]
    writer.writerow(line)
f.close()