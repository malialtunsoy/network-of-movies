import json

movie_cast = {}
with open('data/json/movie_cast_json.txt') as json_file:
    data = json.load(json_file)
    movie_cast = data

movie_director = {}
with open('data/json/movie_director_json.txt') as json_file:
    data = json.load(json_file)
    movie_director = data

cast = []

for movie in movie_cast:
    for actor in movie_cast[movie]:
        if actor not in cast:
            cast.append(actor)

cast_starring_count = {}
for actor in cast:
    cast_starring_count[actor] = 0

for movie in movie_cast:
    for actor in movie_cast[movie]:
        cast_starring_count[actor] += 1

cast_starring_more_than_ones = []
for actor in cast_starring_count:
    if cast_starring_count[actor] > 1:
        cast_starring_more_than_ones.append(actor)

movie_cast_dir = {}

for movie in movie_cast:
    movie_cast_dir[movie] = {}
    cast_of_movie = []
    for actor in movie_cast[movie]:
        if actor in cast_starring_more_than_ones:
            cast_of_movie.append(actor)
    movie_cast_dir[movie]["director"] = movie_director[movie]
    movie_cast_dir[movie]["cast"] = cast_of_movie

# write to JSON file
with open('data/json/movie_cast_director_json.txt', 'w') as outfile:
    json.dump(movie_cast_dir, outfile)